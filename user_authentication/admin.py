from django.contrib import admin
from .models import User
# from django.contrib.auth.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'phone', 'email', 'address')

admin.site.register(User, UserAdmin)
