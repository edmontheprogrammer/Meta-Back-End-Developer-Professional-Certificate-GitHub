from django.contrib import admin
from .models import Categories, MenuItems, Orders

# Register your models here.
admin.site.register(Categories)
admin.site.register(MenuItems)
admin.site.register(Orders)
