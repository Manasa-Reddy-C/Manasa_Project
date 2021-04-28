from django.contrib import admin
from django.shortcuts import render
from App.models import Login
@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display=('Source','Name','Category')
    



    


#admin.site.register(Login,LoginAdmin)

# Register your models here.
