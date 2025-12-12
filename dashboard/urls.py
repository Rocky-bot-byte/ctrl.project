from django.urls import path
from . import views

urlpatterns = [
    path('client/', views.client_dashboard, name='client_dashboard'),
    path('client/profile/', views.client_profile, name='client_profile'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('notification/<int:notification_id>/read/', views.mark_notification_read, name='mark_notification_read'),
]