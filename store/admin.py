from django.contrib import admin

from store.models import Plant, Tool, PlantComment, ToolComment

# Register your models here.
admin.site.register(Plant)
admin.site.register(Tool)
admin.site.register(PlantComment)
admin.site.register(ToolComment)
