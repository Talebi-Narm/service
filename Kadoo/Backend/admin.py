from django.contrib import admin
from .models import Plant, Tool, Tag, Album, Image

admin.site.register(Plant)
admin.site.register(Tool)
admin.site.register(Tag)

class Images(admin.StackedInline):
    model = Image

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [Images]

    class Meta:
        model = Album
