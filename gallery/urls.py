from django.contrib import admin
from django.urls import path
from . import views
from .views import CreateGalleryView

urlpatterns = [
    path('load_image', CreateGalleryView.as_view()),
]
