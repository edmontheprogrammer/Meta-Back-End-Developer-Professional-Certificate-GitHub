# URL Namingspacing and Views:
#
# This reading expalins the use of named URLs in the "URLConf" of a Django app and how tue use of a namespace helps in
# resolving the same URL name in more than one app.
#
#  In each app, there is a "urls.py" file that defines the list onf the URL patterns for that app. Each pattern is
# constructed by django.urls.path() function. Its arguments are a URL path string, the name of the view function to be
# mapped to it and an optional argument name.
#
# The following is the "urls.py" of an app:  ##

# demoapp/urls.py
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]

# It is included in the project's urlpatterns.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demoapp.urls')),
]

#  Normally, the client's request URL is mapped against the funciton so that the application flow is directed toward it.
# The URL references used internally by the application are hard-coded strings.
# For example, a form template's action attribute points towards "/demoapp/login" URL so that when the form is submitted
# , the login view mapped to this URL is invoed.  ##
# <form action='/demoapp/login', method='POST'>

# </form>

# reverse() function:
#   However, the hard-coded URLs make the applicaiton less scalable and difficult to maintain as the project grows. In such
# a case, you can obtain the URL from the name parameter used in the path() function.
#
# Starting the Django shell.  ##
# python manage.py shell
# Django's "reverse()" function returns the URL path to which it is mapped.
# from django.urls import reverse
# reverse('index')
# '/demo/'
#
#
# The problem comes when the view function of the same name is defined in more than one app. This is where the idea of a
# "namespace" is needed.
#
# Application namespace:
#   The application namespace is created by the defining "app_name" variable in the application's "urls.py" and assigning
# it the name of the app. In the "demoapp/urls.py" script, make the change using the following code:
#  ##

app_name = 'demoapp'
urlpatterns = [
    path('', views.index, name='index'),
]

# The "app_name" defines the application namespace so that the views in this app are identified by it.
#
# To obtain the URL path of the "index()" function, call the "reverse()" function by prepending the namespace to it
# reverse('demoapp:index')
# '/demo/'
#
# To appericate the advantage of defining a namespace, add another app in the project, for example, newapp.
#
# Instance namespace:
#   You can also use the namespace parameter in the "include()" function while adding an app's "urlpattern" to that of
# a project.  ##
urlpatterns = [
    path('demo/', include('demoapp.urls', namespace='demoapp')),
]

# This namespace is calle the "instance namespace"

# Using namespace in view:
#   Suppose you want to the user to be conditionally redirected to the login view from inside another view. You need to
# obtain the URL of the login view and send the control to it with "HttpResponsePermanentRedirect"
#  ##


def myview(request):
    return HttpResponsePermanentRedirect(reverse
                                         ('demoapp:login'))

# 
