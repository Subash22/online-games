from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('booking/view/<int:id>', view_booking, name='view_booking'),
    path('booking/edit/<int:id>', EditBookingView.as_view(), name='edit_booking'),
    path('booking/delete/<int:id>', delete_booking, name='delete_booking'),
    path('profile', ProfileView.as_view(), name='profile'),
]
