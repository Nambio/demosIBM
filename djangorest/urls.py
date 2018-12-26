# djangorest/urls.py
# This is the main urls.py. It should'nt be mistaken for the urls.py in the api directory

from django.conf.urls import url, include
from django.contrib  import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('api.urls')) # Add this line
]
