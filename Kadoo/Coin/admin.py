from django.contrib import admin

from Coin.models import CoinManagementModel, LastSeenLogModel, LastWateringLogModel

class CoinManagmentAdminConfig(admin.ModelAdmin):
    model = CoinManagementModel
    search_fields = ('user', 'coin_vlaue', 'used_plant_count', 'last_update')
    list_filter = ('user', 'coin_vlaue', 'used_plant_count', 'last_update')
    ordering = ('-last_update',)
    list_display = ('user', 'coin_vlaue', 'used_plant_count', 'last_update')
    fieldsets = (
        (None, {'fields': ('user', 'coin_vlaue', 'used_plant_count')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'coin_vlaue', 'used_plant_count')}
         ),
    )

admin.site.register({CoinManagementModel}, CoinManagmentAdminConfig)
admin.site.register(LastSeenLogModel)
admin.site.register(LastWateringLogModel)
