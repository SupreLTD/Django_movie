from django.contrib import admin
from .models import Movie, Genre, Actor, MovieShots, Category, Rating, RatingStar, Reviews

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(MovieShots)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
