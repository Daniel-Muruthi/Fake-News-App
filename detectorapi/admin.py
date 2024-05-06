from django.contrib import admin
from .models import News, Contact
from django.contrib.admin import AdminSite
# Register your models here.



admin.site.register(News)
admin.site.register(Contact)
