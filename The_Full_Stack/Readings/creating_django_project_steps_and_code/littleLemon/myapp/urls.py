from django.urls import path
from .views import ratings, form_view


urlpatterns = [
    path('', ratings),
    path('blog', form_view),
]
