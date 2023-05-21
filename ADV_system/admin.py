from django.contrib import admin
from .models import Ad, Advertiser


class ADVERTISER(admin.ModelAdmin):
    list_display = ('name', 'site',)


class AD(admin.ModelAdmin):
    list_display = ('title', 'advertiser',)


admin.site.register(Advertiser, ADVERTISER)
admin.site.register(Ad, AD)
