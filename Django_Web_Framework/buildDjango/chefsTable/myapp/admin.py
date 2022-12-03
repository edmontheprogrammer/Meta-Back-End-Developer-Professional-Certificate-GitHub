from django.contrib import admin
from . models import Menu, Menuitems, Drinks
# Register your models here.

admin.site.register(Drinks)
admin.site.register(Menu)
admin.site.register(Menuitems)
