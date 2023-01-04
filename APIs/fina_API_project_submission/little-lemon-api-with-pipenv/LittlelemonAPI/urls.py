from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('littlelemons', views.littlelemons)
    path('littlelemons', views.Littlelemon.as_view()),
    path('categories', views.categories),
    path('menuitems', views.menu_items),
    path('orders', views.orders),
    # path('orderitems', views.order_items),
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check)
]


#  API endpoints
# Here are all the required API routes for this project grouped into several categories.

# User registration and token generation endpoints
# You can use Djoser in your project to automatically create the following endpoints and
# functionalities for you.
