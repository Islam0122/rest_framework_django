from django.db import models


class Director(models.Model):
    # img = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @property
    def movie_count(self):
        movies = self.movies.all().count()
        return movies


class Movie(models.Model):
    # img = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    duration = models.IntegerField()
    create_data = models.DateTimeField(auto_now_add=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")

    @property
    def rating(self):
        count = self.reviews.all().count()
        stars = sum([i.stars for i in self.reviews.all()])
        return stars // count

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        try:
            return self.director.name
        except:
            return None


STARS_CHOICES = ((1, 1),
                 (2, 2),
                 (3, 3),
                 (4, 4),
                 (5, 5)
                 )


class Review(models.Model):
    text = models.CharField(max_length=255)
    stars = models.IntegerField(choices=(STARS_CHOICES))

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.movie.title
