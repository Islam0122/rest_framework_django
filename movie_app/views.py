
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.serializers import MovieSerializers, DirectorSerializers, ReviewSerializers
from movie_app.models import Movie, Director, Review


@api_view(['GET', 'POST'])
def director_api_list_view(request):
    if request.method == 'GET':

        directors = Director.objects.all()
        data = DirectorSerializers(instance=directors, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        name = request.data.get('name')

        director_ = Director.objects.create(name=name)

        return Response(data=DirectorSerializers(director_).data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, director_id):
    director = Director.objects.get(id=director_id)
    if request.method == 'GET':
        data = DirectorSerializers(instance=director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Product removed!'})
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        return Response(data=DirectorSerializers(director).data)


@api_view(['GET','POST'])
def movie_api_list_view(request):
    if request.method == 'GET':
       movie = Movie.objects.all()
       data = MovieSerializers(instance=movie, many=True).data
       return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description =request.data.get('description')
        is_active = request.data.get('is_active')
        duration = request.data.get('duration')
        create_data = request.data.get('create_data')
        director_id =request.data.get('director_id')
        movie= Movie.objects.create(title=title,description=description,is_active=is_active,duration=duration,
                                    create_data=create_data,director_id=director_id)

        return Response(data=MovieSerializers(movie).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'GET':
         data = MovieSerializers(instance=movie).data
         return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Product removed!'})
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description =request.data.get('description')
        movie.is_active = request.data.get('is_active')
        movie.duration = request.data.get('duration')
        movie.create_data = request.data.get('create_data')
        movie.director_id =request.data.get('director_id')
        return Response(data=MovieSerializers(movie).data)


@api_view(['GET', 'POST'])
def review_api_list_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializers(instance=reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        review = Review.objects.create(text=text, stars=stars ,  movie_id=movie_id)

        return Response(data=ReviewSerializers(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'GET':
        data = ReviewSerializers(instance=review).data
        return Response(data=data)
    elif request.method == 'DELETE':
          review.delete()
          return Response(status=status.HTTP_204_NO_CONTENT,
                    data={'message': 'Product removed!'})

    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        return Response(data=ReviewSerializers(review).data)



