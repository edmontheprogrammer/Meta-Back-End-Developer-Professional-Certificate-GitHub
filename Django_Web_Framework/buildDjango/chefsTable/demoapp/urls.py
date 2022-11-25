from django.urls import path
from . import views

# creating a list named "urlpatterns" that maps a link to the "index()" function that
# we created in the "views.py" file
urlpatterns = [
    path('', views.demoappHome, name='index'),
]
