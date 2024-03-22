from django.urls import path
from . import views

urlpatterns = [
    path("", views.Rooms.as_view()),
    path("<int:pk>/", views.RoomDetail.as_view()),
    path("<int:pk>/photos/", views.RoomPhotos.as_view()),
]