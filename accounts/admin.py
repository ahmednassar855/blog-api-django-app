from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import customUserChangeForm , customUserCreationForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = customUserCreationForm
    form = customUserChangeForm
    model = CustomUser
    list_display = ["email",
                    "username",
                    "name",
                    "is_staff",]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(CustomUser, CustomUserAdmin)