from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("home", views.index, name='home'),
    path("about", views.about, name='about'),
    path("projects", views.projects, name='projects'),
    path("portfolio", views.portfolio, name='portfolio'),
    path("hireme", views.hireme, name='hireme'),
    path("Blog", views.Blog, name='Blog'),
]
