from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    model = Account
    search_fields = ('email', 'username', 'first_name','last_name')
    list_filter = ('email', 'username', 'first_name','last_name', 'is_active', 'is_staff')
    ordering = ()
    list_display = ('id','email', 'username', 'first_name', 'last_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff','is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_admin','is_staff')}
         ),
    )

    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)