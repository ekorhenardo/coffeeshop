from django.contrib import admin

from .models import Type, Menu, Orders

admin.site.register(Type)
admin.site.register(Menu)
admin.site.register(Orders)