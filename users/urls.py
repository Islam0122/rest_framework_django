from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration_user_api_view),
    path('login/', views.login_user_api_view),
    path('confirm/', views.confirm_user_api_view),
    ]