from django.contrib import admin
from django.urls import path
from .views import FeedBackView, DoneView, FeedBackUpdateView, ListFeedBack, DetailFeedBack

urlpatterns = [
    path('', FeedBackView.as_view()),
    path('done', DoneView.as_view()),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('detail/<int:id_feedback>', DetailFeedBack.as_view())
]
