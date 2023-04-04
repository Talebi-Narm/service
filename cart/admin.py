# from django.contrib import admin
# from .models import OrderModel, PlantCartModel, ToolCartModel
# from django.contrib import admin
# from django.forms import Textarea
#
# class PlantUserAdminConfig(admin.ModelAdmin):
#     model = PlantCartModel
#     search_fields = ('user', 'plant_item', 'plant_count', 'description', 'created', 'modified', 'is_approved')
#     list_filter = ('user', 'plant_item', 'plant_count', 'description', 'created', 'modified', 'is_approved')
#     ordering = ('-created',)
#     list_display = ('user', 'plant_item', 'plant_count', 'description', 'created', 'modified', 'is_approved')
#     fieldsets = (
#         (None, {'fields': ('user', 'plant_item', 'plant_count', 'is_approved')}),
#         ('Personal', {'fields': ('description',)}),
#     )
#     formfield_overrides = {
#          PlantCartModel.description: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('user', 'plant_item', 'plant_count', 'description', 'created', 'modified', 'is_approved')}
#          ),
#     )
#
# class ToolUserAdminConfig(admin.ModelAdmin):
#     model = ToolCartModel
#     search_fields = ('user', 'tool_item', 'tool_count', 'description', 'created', 'modified', 'is_approved')
#     list_filter = ('user', 'tool_item', 'tool_count', 'description', 'created', 'modified', 'is_approved')
#     ordering = ('-created',)
#     list_display = ('user', 'tool_item', 'tool_count', 'description', 'created', 'modified', 'is_approved')
#     fieldsets = (
#         (None, {'fields': ('user', 'tool_item', 'tool_count', 'is_approved')}),
#         ('Personal', {'fields': ('description',)}),
#     )
#     formfield_overrides = {
#          ToolCartModel.description: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('user', 'tool_item', 'tool_count', 'description', 'created', 'modified', 'is_approved')}
#          ),
#     )
#
# class OrderAdminConfig(admin.ModelAdmin):
#     model = OrderModel
#     search_fields = ('user', 'order_plants', 'order_tools', 'status', 'total_price', 'description', 'created', 'is_delivered')
#     list_filter = ('user', 'order_plants', 'order_tools', 'status', 'total_price', 'description', 'created', 'is_delivered')
#     ordering = ('-created',)
#     list_display = ('user', 'status', 'total_price', 'description', 'created', 'is_delivered')
#     fieldsets = (
#         (None, {'fields': ('user', 'order_plants', 'order_tools', 'status', 'total_price', 'is_delivered')}),
#         ('Personal', {'fields': ('description',)}),
#     )
#     formfield_overrides = {
#          ToolCartModel.description: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('user', 'order_plants', 'order_tools', 'status', 'total_price', 'description', 'created', 'is_delivered')}
#          ),
#     )
#
#
# admin.site.register({PlantCartModel}, PlantUserAdminConfig)
# admin.site.register({ToolCartModel}, ToolUserAdminConfig)
# admin.site.register({OrderModel}, OrderAdminConfig)