"""
URL configuration for month5_hw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # режиссеров
    # path('api/v1/directors/', views.director_api_list_view),
    # path('api/v1/directors/<int:director_id>/', views.director_detail_api_view),
    path('api/v1/directors_cvb/', views.DirectorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/directors_cvb/<int:id>/',
         views.DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # фильмов
    # path('api/v1/movies/', views.movie_api_list_view),
    # path('api/v1/movies/<int:movie_id>/', views.movie_detail_api_view),
    path('api/v1/movies_cvb/', views.MOVIEViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/movies_cvb/<int:id>/',
         views.MOVIEViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # отзывов
    # path('api/v1/reviews/', views.review_api_list_view),
    # path('api/v1/reviews/<int:review_id>/', views.review_detail_api_view),
    path('api/v1/reviews_cvb/', views.ReviewViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/reviews_cvb/<int:id>/',
         views.ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # users
    path('api/v1/users/', include('users.urls'))

]
