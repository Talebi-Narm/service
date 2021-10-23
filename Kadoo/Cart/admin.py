from django.contrib import admin
from .models import PlantCartModel
from django.contrib import admin
from django.forms import Textarea

class PlantUserAdminConfig(admin.ModelAdmin):
    model = PlantCartModel
    search_fields = ('user', 'plant_item', 'plant_count', 'description', 'created', 'modified')
    list_filter = ('user', 'plant_item', 'plant_count', 'description', 'created', 'modified')
    ordering = ('-created',)
    list_display = ('user', 'plant_item', 'plant_count', 'description', 'created', 'modified')
    fieldsets = (
        (None, {'fields': ('user', 'plant_item', 'plant_count')}),
        ('Personal', {'fields': ('description',)}),
    )
    formfield_overrides = {
         PlantCartModel.description: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'plant_item', 'plant_count', 'description', 'created', 'modified')}
         ),
    )

admin.site.register({PlantCartModel}, PlantUserAdminConfig)