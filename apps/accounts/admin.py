from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','is_superuser','is_active')
    list_filter = ('is_superuser','is_active','date_joined')

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
