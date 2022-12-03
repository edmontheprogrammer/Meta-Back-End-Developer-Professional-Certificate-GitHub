from django.db import models

# Create your models here.


class Drinks(models.Model):
    # DrinksID = models.IntegerField(primary_key=True)
    drink = models.CharField(max_length=200)
    price = models.IntegerField()


class Menuitems(models.Model):
    #  MenuitemsID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    year = models.IntegerField()


class Menu(models.Model):
    # MenuID = models.IntegerField(primary_key=True) ???
    # MenuitemsID = models.OneToOneField(
    #     Menuitems, on_delete=models.CASCADE
    # )
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " : " + self.cuisine
