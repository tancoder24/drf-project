from django.contrib import admin
from django.urls import path, include

from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name="movie_list"),
    path('detail/<int:pk>', MovieDetailAV.as_view(), name="movie_detail"),
]
