from django.contrib import admin
from .models import Park, Campground, Campsite, Feature, District, Region, CampsiteClass, CampsiteBooking, Booking,PromoArea, CampsiteRate, Contact, Rate

@admin.register(CampsiteClass)
class CampsiteClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):
    list_display = ('name','district')
    ordering = ('name',)
    list_filter = ('district',)
    search_fields = ('name',)

@admin.register(Campground)
class CampgroundAdmin(admin.ModelAdmin):
    list_display = ('name','park','promo_area','campground_type','site_type')
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('campground_type','site_type')

@admin.register(Campsite)
class CampsiteAdmin(admin.ModelAdmin):
    list_display = ('name','campground',)
    ordering = ('name',)
    list_filter = ('campground',)
    search_fields = ('name',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('arrival','departure','campground','legacy_id','legacy_name','cost_total')
    ordering = ('-arrival',)
    search_fileds = ('arrival','departure')
    list_filter = ('arrival','departure')

@admin.register(CampsiteBooking)
class CampsiteBookingAdmin(admin.ModelAdmin):
    list_display = ('campsite','date','booking','booking_type')
    ordering = ('-date',)
    search_fields = ('date',)
    list_filter = ('campsite','booking_type')

@admin.register(CampsiteRate)
class CampsiteRateAdmin(admin.ModelAdmin):
    list_display = ('campsite','rate','allow_public_holidays')
    list_filter = ('campsite','rate','allow_public_holidays')
    search_fields = ('campground__name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number')
    search_fields = ('name','phone_number')

admin.site.register(Rate)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(PromoArea)

