from django.contrib import admin

from cart.models import PlantCart, ToolCart


@admin.register(PlantCart)
class PlantCartAdmin(admin.ModelAdmin):
    pass


@admin.register(ToolCart)
class ToolCartAdmin(admin.ModelAdmin):
    pass
