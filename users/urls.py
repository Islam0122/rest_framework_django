from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Registration_userViewSet.as_view({'post': 'create'})),
    path('login/', views.login_userViewSet.as_view({'post': 'post'})),
    path('confirm/', views.confirm_userViewPost.as_view())
]
