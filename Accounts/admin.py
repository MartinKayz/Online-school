from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from .forms import UserAdminChangeForm, RegisterForm
User = get_user_model()


class UserAdmin(admin.ModelAdmin):

    form = UserAdminChangeForm  # update View
    add_form = RegisterForm  # create view
    list_display = ['email', 'admin']
    list_filter = ('admin', 'staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ("UserName ", {"fields": ('username',)}),
        ("Permissions", {"fields": ('admin', 'staff',)}),
    )
    add_fieldsets = (
        (
            None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email','username']
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
