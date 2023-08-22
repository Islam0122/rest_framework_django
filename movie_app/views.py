from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.serializers import MovieSerializers, DirectorSerializers, ReviewSerializers
from movie_app.models import Movie, Director, Review


@api_view(['GET'])
def director_api_list_view(request):
    director = Director.objects.all()
    data = DirectorSerializers(instance=director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail_api_view(request, director_id):
    director = Director.objects.get(id=director_id)
    data = DirectorSerializers(instance=director).data
    return Response(data=data)


@api_view(['GET'])
def movie_api_list_view(request):
    movie = Movie.objects.all()
    data = MovieSerializers(instance=movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    data = MovieSerializers(instance=movie).data
    return Response(data=data)


@api_view(['GET'])
def review_api_list_view(request):
    review = Review.objects.all()
    data = ReviewSerializers(instance=review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, review_id):
    review = Review.objects.get(id=review_id)
    data = ReviewSerializers(instance=review).data
    return Response(data=data)

