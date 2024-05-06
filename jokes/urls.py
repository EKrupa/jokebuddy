
from django.contrib import admin
from django.urls import path
from jokes.views import home, getResponse



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('getResponse', getResponse, name='getResponse' )
]
