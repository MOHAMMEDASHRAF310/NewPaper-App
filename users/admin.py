from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm,CustomUserCreationForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
admin.site.register(CustomUser,CustomUserAdmin)