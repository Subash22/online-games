from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', user_register, name='user_register'),
]
