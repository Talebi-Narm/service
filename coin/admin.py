from django.contrib import admin

from Coin.models import CoinManagementModel, LastSeenLogModel, LastWateringLogModel

class CoinManagmentAdminConfig(admin.ModelAdmin):
    model = CoinManagementModel
    search_fields = ('user', 'coin_value', 'used_plant_count', 'last_update')
    list_filter = ('user', 'coin_value', 'used_plant_count', 'last_update')
    ordering = ('-last_update',)
    list_display = ('user', 'coin_value', 'used_plant_count', 'last_update')
    fieldsets = (
        (None, {'fields': ('user', 'coin_value', 'used_plant_count')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'coin_value', 'used_plant_count')}
         ),
    )


class LastSeenLogAdminConfig(admin.ModelAdmin):
    model = LastSeenLogModel
    search_fields = ('user', 'date')
    list_filter = ('user', 'date')
    ordering = ('-date',)
    list_display = ('user', 'date')
    fieldsets = (
        (None, {'fields': ('user',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'date')}
         ),
    )


class LastWateringLogAdminConfig(admin.ModelAdmin):
    model = LastWateringLogModel
    search_fields = ('user', 'date')
    list_filter = ('user', 'date')
    ordering = ('-date',)
    list_display = ('user', 'date')
    fieldsets = (
        (None, {'fields': ('user',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'date')}
         ),
    )

admin.site.register({CoinManagementModel}, CoinManagmentAdminConfig)
admin.site.register({LastSeenLogModel}, LastSeenLogAdminConfig)
admin.site.register({LastWateringLogModel}, LastWateringLogAdminConfig)
