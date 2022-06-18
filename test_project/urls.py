from django.urls import re_path as url 
from django.urls import include
 
urlpatterns = [ 
    url(r'^', include('booksapi.urls')),
]