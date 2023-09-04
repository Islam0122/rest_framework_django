# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from movie_app.models import Movie, Director, Review
from movie_app.serializers import MovieSerializers, DirectorSerializers, ReviewSerializers, DirectorValidateSerializer, \
    ReviewValidateSerializer, MovieValidateSerializer

'''DIRECTOR'''
# @api_view(['GET', 'POST'])
# def director_api_list_view(request):
#     if request.method == 'GET':
#
#         directors = Director.objects.all()
#         data = DirectorSerializers(instance=directors, many=True).data
#         return Response(data=data)
#
#     elif request.method == 'POST':
#         # Step 0. Validation
#         serializer = DirectorValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         # Step 1. Get data from validated data
#         name = serializer.validated_data.get('name')
#         # Step 2. Create director
#         director_ = Director.objects.create(name=name)
#         # Step 3. Return created object
#         return Response(data=DirectorSerializers(director_).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, director_id):
#     try:
#         director = Director.objects.get(id=director_id)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'Product not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = DirectorSerializers(instance=director).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT,
#                         data={'message': 'Product removed!'})
#     elif request.method == 'PUT':
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         director.name = serializer.validated_data.get('name')
#         return Response(data=DirectorSerializers(director).data)
'''Director-> CBV -> MODEL_VIEW_SET'''


class DirectorViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director = self.get_object()
        director.name = serializer.validated_data.get('name')

        return Response(data=self.serializer_class(director, many=False).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director = Director.objects.create(
            name=request.data.get('name'))

        return Response(data=self.serializer_class(director, many=False).data, status=status.HTTP_201_CREATED)


'''MOVIE '''
# @api_view(['GET', 'POST'])
# def movie_api_list_view(request):
#     if request.method == 'GET':
#         movie = Movie.objects.select_related('director') \
#             .prefetch_related('reviews').all()
#         data = MovieSerializers(instance=movie, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         is_active = serializer.validated_data.get('is_active')
#         duration = serializer.validated_data.get('duration')
#         create_data = serializer.validated_data.get('create_data')
#         director_id = serializer.validated_data.get('director_id')
#         movie = Movie.objects.create(title=title, description=description, is_active=is_active, duration=duration,
#                                      create_data=create_data,director_id=director_id)
#         return Response(data=MovieSerializers(movie).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, movie_id):
#     try:
#         movie = Movie.objects.get(id=movie_id)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'Product not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = MovieSerializers(instance=movie).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT,
#                         data={'message': 'Product removed!'})
#     elif request.method == 'PUT':
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie.title = serializer.validated_data.get('title')
#         movie.description = serializer.validated_data.get('description')
#         movie.is_active = serializer.validated_data.get('is_active')
#         movie.duration = serializer.validated_data.get('duration')
#         movie.create_data = serializer.validated_data.get('create_data')
#         movie.director_id = serializer.validated_data.get('director_id')
#         return Response(data=MovieSerializers(movie).data)
'''MOVIE -> CBV -> MODEL_VIEW_SET'''


class MOVIEViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = Movie.objects.all().prefetch_related('reviews').select_related('director')
    serializer_class = MovieSerializers
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie = self.get_object()
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.is_active = serializer.validated_data.get('is_active')
        movie.duration = serializer.validated_data.get('duration')
        movie.create_data = serializer.validated_data.get('create_data')
        movie.director_id = serializer.validated_data.get('director_id')

        return Response(data=self.serializer_class(movie, many=False).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie = Movie.objects.create(
            title=serializer.validated_data.get('title'),
            description=serializer.validated_data.get('description'),
            is_active=serializer.validated_data.get('is_active'),
            duration=serializer.validated_data.get('duration'),
            create_data= serializer.validated_data.get('create_data'),
            director_id =serializer.validated_data.get('director_id'))

        return Response(data=self.serializer_class(movie, many=False).data, status=status.HTTP_201_CREATED)


'''REVIEW'''
# @api_view(['GET', 'POST'])
# def review_api_list_view(request):
#     serializer = ReviewValidateSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response(status=status.HTTP_400_BAD_REQUEST,
#                         data={'errors': serializer.errors})
#
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         data = ReviewSerializers(instance=reviews, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         text = request.data.get('text')
#         stars = request.data.get('stars')
#         movie_id = request.data.get('movie_id')
#         review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
#
#         return Response(data=ReviewSerializers(review).data)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, review_id):
#     try:
#         review = Review.objects.get(id=review_id)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'Product not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         data = ReviewSerializers(instance=review).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT,
#                         data={'message': 'Product removed!'})
#
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         review.text = serializer.validated_data.get('text')
#         review.stars = serializer.validated_data.get('stars')
#         review.movie_id = serializer.validated_data.get('movie_id')
#         return Response(data=ReviewSerializers(review).data)

'''REVIEW -> CBV -> MODEL_VIEW_SET'''


class ReviewViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review = self.get_object()

        review.text = serializer.validated_data.get('text')
        review.stars = serializer.validated_data.get('stars')
        review.movie_id = serializer.validated_data.get('movie_id')
        return Response(data=self.serializer_class(review, many=False).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review = Review.objects.create(
            text=request.data.get('text'),
            stars=request.data.get('stars'),
            movie_id=request.data.get('movie_id'))
        return Response(data=self.serializer_class(review, many=False).data, status=status.HTTP_201_CREATED)
