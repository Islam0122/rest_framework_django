from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Movie, Review, Director


class DirectorSerializers(serializers.ModelSerializer):
    movie_count = serializers.IntegerField()

    class Meta:
        model = Director
        fields = 'id name movie_count'.split()

    def get_movie_count(self, director):
        return director.movie_count


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=1, max_length=100)


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars movie_id'.split()


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, min_length=1, max_length=255)
    stars = serializers.IntegerField(required=True,min_value=1, max_value=5)
    movie_id = serializers.IntegerField()

    def validate_movie_id(self, movie_id):  # 10
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Category does not exists!')
        return movie_id


class MovieSerializers(serializers.ModelSerializer):
    director = DirectorSerializers()
    reviews = ReviewSerializers(many=True)
    rating = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = 'title description duration create_data director director_name reviews rating'.split()

    def get_rating(self, movie):
        return movie.rating
class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=1, max_length=100)
    description = serializers.CharField(required=False)
    is_active = serializers.BooleanField(default=True)
    duration = serializers.IntegerField()
    director_id= serializers.IntegerField()

    def validate_director_id(self, director_id):  # 10
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exists!')
        return director_id






