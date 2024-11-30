from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-request/', views.create_request, name='create_request'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update-request/<int:pk>/', views.update_request_status, name='update_request_status'),
]
