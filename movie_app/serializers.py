from rest_framework import  serializers
from .models import Movie ,Review,Director

class movie_serializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
class Director_serializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
class Review_serializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'