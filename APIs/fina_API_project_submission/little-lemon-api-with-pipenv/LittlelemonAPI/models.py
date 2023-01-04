from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Creating the "Category" table with its attributes "slug" and "title"


class Categories(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)


# Creating the "MenuItem" table with its attributes "title", "price", "features",
# and "category".
# Note 1: "category" is a foreign key in the "MenuItem" table. You can query, look up
# information on the "Category" table using the "MenuItem" table
class MenuItems(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)


# Creating the "Cart" table with its attributes "user", "menuitem", "quantity",
# "unit_price", and "price"
# Note 2: "user" and "menuitem" are foreign keys referencing the primary key of
#  "MenuItem" and "User" tables. You can access info. from boths tables here.
# here in the "Cart" table.
# Note 3: All Django models have a default primary key field named "id".
# Note 4: The "Meta" class here is creating a unique index for the "Cart" table ##
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     menuitem = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
#     quantity = models.SmallIntegerField(),
#     unit_price = models.DecimalField(max_digits=6, decimal_places=2)
#     price = models.DecimalField(max_digits=6, decimal_places=2)

#     class Meta:
#         unique_together = ('menuitem', 'user')

# Creating "Order" table with its attributes "user", "delivery_crew", "status",
# "total" and "date".
# Note 1: "delivery_crew" is a foreign key to the the "User" table. You can access
#  info. on the "User" table from here, the "Order" table ##


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)


# Creating "OrderItem" table with its attributes "order" and "menuitem".
# Note 1: The "OrderItem" table's attributes, "order" and "menuitem" , are foreign
# keys linking the "User" and "MenuItem" tables to the "OrderItem" table. You can
# combine, access, information from both tables here in the "OrderItem" table.
# Note 2:
# #   The "Meta" class here is creating a unique index for the "OrderItem" table. ##
# class OrderItems(models.Model):
#     order = models.ForeignKey(User, on_delete=models.CASCADE)
#     menuitem = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
#     quanity = models.SmallAutoField()
#     unit_price = models.DecimalField(max_digits=6, decimal_places=2)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     order = models.ForeignKey(Orders, on_delete=models.PROTECT, default=1)

#     class Meta:
#         unique_together = ('order', 'menuitem')
