from django.db import models


class Director(models.Model):
    # img = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Movie(models.Model):
    #img = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    duration = models.IntegerField()
    create_data = models.DateTimeField(auto_now_add=True)
    modified_data = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    def __str__(self):
        return  self.title

class Review(models.Model):
        text = models.CharField(max_length=255)
        name = models.CharField(max_length=20)
        movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

        def __str__(self):
            return f'{self.text}-> {self.movie.title}'
