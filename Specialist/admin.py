# from django.contrib import admin
# from django.forms.widgets import Textarea
#
# from Specialist.models import SpecilistFields
#
# class SpecialistFieldAdminConfig(admin.ModelAdmin):
#     model = SpecilistFields
#     search_fields = ('user', 'id_code', 'birth_date', 'degree', 'major', 'phone_number', 'about','address','is_online', 'rate')
#     list_filter = ('user', 'id_code', 'birth_date', 'degree', 'major', 'phone_number', 'about','address','is_online', 'rate')
#     ordering = ('-user',)
#     list_display = ('user', 'id_code', 'birth_date', 'degree', 'major', 'phone_number', 'about','address','is_online', 'rate')
#     fieldsets = (
#         (None, {'fields': ('user', 'id_code', 'birth_date', 'degree', 'major', 'phone_number', 'is_online', 'rate')}),
#         ('Personal', {'fields': ('address','about')}),
#     )
#     formfield_overrides = {
#          SpecilistFields.address: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('user', 'id_code', 'birth_date', 'degree', 'major', 'phone_number', 'about','address','is_online', 'rate')}
#          ),
#     )
#
# admin.site.register({SpecilistFields}, SpecialistFieldAdminConfig)