from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
    path("add-friend", UserAddFriend.as_view(), name="add-friend"),
    path("play", UserPlay.as_view(), name="play"),
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile")
]
