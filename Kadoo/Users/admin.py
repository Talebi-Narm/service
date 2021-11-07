from django.contrib import admin
from .models import MemberFields, NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('type', 'email', 'user_name', 'first_name', 'last_name')
    list_filter = ('type', 'email', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'type', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('type', 'email', 'user_name', 'first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('type', 'email', 'user_name', 'first_name','last_name', 'password1', 'password2','is_active', 'is_staff')}
         ),
    )

class MemberFieldAdminConfig(admin.ModelAdmin):
    model = MemberFields
    search_fields = ('user', 'credit_value', 'address', 'phone_number')
    list_filter = ('user', 'credit_value', 'address', 'phone_number')
    ordering = ('-user',)
    list_display = ('user', 'credit_value', 'address', 'phone_number')
    fieldsets = (
        (None, {'fields': ('user', 'credit_value','phone_number')}),
        ('Personal', {'fields': ('address',)}),
    )
    formfield_overrides = {
         MemberFields.address: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'credit_value', 'address', 'phone_number')}
         ),
    )


admin.site.register({NewUser}, UserAdminConfig)
admin.site.register({MemberFields}, MemberFieldAdminConfig)

