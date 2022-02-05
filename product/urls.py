from django.urls import path

from .views import homepage

app_name = 'product'
urlpatterns = [
    path('', homepage, name='home'),
]
