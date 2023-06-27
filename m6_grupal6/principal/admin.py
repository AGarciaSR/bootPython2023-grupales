from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from principal.models import AppUser

admin.site.unregister(User)

class AppUserInline(admin.StackedInline):
    model = AppUser
    can_delete = False
    verbose_name_plural = "appuser"

class AppUserAdmin(UserAdmin):
    inlines = [ AppUserInline, ]

admin.site.register(User, AppUserAdmin)
