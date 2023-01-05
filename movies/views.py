from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MoviesView(ListView):
    """Film list view"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'


class MovieDetailView(DetailView):
    """Full film description"""
    model = Movie
    slug_field = 'url'

