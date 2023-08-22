from rest_framework import serializers
from .models import Movie, Review, Director


class DirectorSerializers(serializers.ModelSerializer):
    movie_count = serializers.IntegerField()

    class Meta:
        model = Director
        fields = 'id name movie_count'.split()

    def get_movie_count(self, director):
        return director.movie_count


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class MovieSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    rating = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = 'title description duration create_data director reviews rating'.split()

    def get_rating(self, movie):
        return movie.rating
