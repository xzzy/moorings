# Prepare the base environment.
FROM ubuntu:22.04 as builder_base_moorings
MAINTAINER asi@dbca.wa.gov.au
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Australia/Perth
ENV PRODUCTION_EMAIL=True
ENV SECRET_KEY="ThisisNotRealKey"
RUN apt-get clean
RUN apt-get update
RUN apt-get install --no-install-recommends -y software-properties-common
RUN apt-get upgrade -y
RUN apt-get install --no-install-recommends -y wget git libmagic-dev gcc g++ binutils libproj-dev gdal-bin tzdata cron rsyslog gunicorn libreoffice gpg-agent 
RUN apt-get install --no-install-recommends -y libpq-dev patch
RUN apt-get install --no-install-recommends -y postgresql-client mtr htop vim ssh
RUN apt-get install --no-install-recommends -y postfix syslog-ng syslog-ng-core
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update
RUN apt-get install --no-install-recommends -y  python3.8 python3.8-distutils python3.8-dev python3-pip python3-setuptools

RUN rm /usr/bin/python3
RUN ln -s /usr/bin/python3.8 /usr/bin/python3
#RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip3 install --upgrade pip
# Install Python libs from requirements.txt.
FROM builder_base_moorings as python_libs_moorings
WORKDIR /app
COPY requirements.txt ./
RUN touch /app/git_hash
RUN pip3 install --no-cache-dir -r requirements.txt
  # Update the Django <1.11 bug in django/contrib/gis/geos/libgeos.py
  # Reference: https://stackoverflow.com/questions/18643998/geodjango-geosexception-error
  #&& sed -i -e "s/ver = geos_version().decode()/ver = geos_version().decode().split(' ')[0]/" /usr/local/lib/python3.6/dist-packages/django/contrib/gis/geos/libgeos.py \
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

COPY libgeos.py.patch /app/
RUN patch /usr/local/lib/python3.8/dist-packages/django/contrib/gis/geos/libgeos.py /app/libgeos.py.patch
RUN rm /app/libgeos.py.patch

# Install the project (ensure that frontend projects have been built prior to this step).
FROM python_libs_moorings

COPY gunicorn.ini manage_mo.py ./
#COPY postfix-main.cf /etc/postfix/main.cf
#RUN update-rc.d postfix enable

#COPY ledger ./ledger
COPY timezone /etc/timezone
ENV TZ=Australia/Perth
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN touch /app/.env
COPY mooring ./mooring
RUN python3 manage_mo.py collectstatic --noinput

RUN mkdir /app/tmp/
RUN chmod 777 /app/tmp/

COPY cron /etc/cron.d/dockercron
COPY startup.sh /
# Cron start
#RUN service rsyslog start
RUN chmod 0644 /etc/cron.d/dockercron
RUN crontab /etc/cron.d/dockercron
RUN touch /var/log/cron.log
RUN service cron start
RUN chmod 755 /startup.sh
# cron end

# kubernetes health checks script
RUN wget https://raw.githubusercontent.com/dbca-wa/wagov_utils/main/wagov_utils/bin/health_check.sh -O /bin/health_check.sh
RUN chmod 755 /bin/health_check.sh

EXPOSE 8080
HEALTHCHECK --interval=1m --timeout=5s --start-period=10s --retries=3 CMD ["wget", "-q", "-O", "-", "http://localhost:8080/"]
CMD ["/startup.sh"]
#CMD ["gunicorn", "mooring.wsgi", "--bind", ":8080", "--config",
