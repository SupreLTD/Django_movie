from django.contrib import admin
from .models import Movie, Genre, Actor, MovieShots, Category, Rating, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInLine(admin.TabularInline):  # StackedInline
    """Display a review class in other models"""
    model = Reviews
    extra = 0
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'age', 'image')


admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
