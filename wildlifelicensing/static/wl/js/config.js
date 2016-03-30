require.config({
    baseUrl: '/static/wl',
    paths: {
        'jQuery': '//static.dpaw.wa.gov.au/static/libs/jquery/2.2.0/jquery.min',
        'bootstrap': '//static.dpaw.wa.gov.au/static/libs/twitter-bootstrap/3.3.6/js/bootstrap.min',
        'bootstrap-datetimepicker': '//static.dpaw.wa.gov.au/static/libs/bootstrap-datetimepicker/4.7.14/js/bootstrap-datetimepicker.min',
        'select2': '//static.dpaw.wa.gov.au/static/libs/select2/3.5.4/select2.min',
        'handlebars': '//static.dpaw.wa.gov.au/static/libs/handlebars.js/4.0.5/handlebars.amd.min',
        'moment': '//static.dpaw.wa.gov.au/static/libs/moment.js/2.9.0/moment.min',
        'parsley': '//static.dpaw.wa.gov.au/static/libs/parsley.js/2.3.5/parsley.min',
        'datatables.net': '//static.dpaw.wa.gov.au/static/libs/datatables/1.10.10/js/jquery.dataTables.min',
        'datatables.bootstrap': '//static.dpaw.wa.gov.au/static/libs/datatables/1.10.10/js/dataTables.bootstrap.min',
        'lodash':'//static.dpaw.wa.gov.au/static/libs/lodash.js/4.5.1/lodash.min',
        'bootstrap.treeView': '//static.dpaw.wa.gov.au/static/libs/bootstrap-treeview/1.2.0/bootstrap-treeview.min'
    },
    shim: {
        'jQuery': {
            exports: '$'
        },
        'bootstrap': {
            deps: ['jQuery']
        },
        'bootstrap-datetimepicker': {
            deps: ['jQuery', 'bootstrap', 'moment']
        },
        'select2': {
            deps: ['jQuery', 'bootstrap']
        },
        'parsley': {
            deps: ['jQuery']
        },
        'datatables.net': {
            deps: ['jQuery']
        },
        'datatables.bootstrap': {
            deps: ['jQuery']
        },
        'bootstrap.treeView': {
            deps: ['bootstrap']
        }
    }
});
