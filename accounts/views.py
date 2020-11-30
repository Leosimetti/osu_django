from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import userProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer

from rest_framework import filters


# Create your views here.

class UserPlay(UpdateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        # print(request.user) is just the name
        user = userProfile.objects.get(user=request.user)
        user.map_plays += 1

        try:
            user.hours_played += float(request.query_params.get('length')) / 3600
            user.total_score += int(request.query_params.get('score'))

            if request.query_params.get('passed') == "true":
                user.successful_map_plays += 1
        except:
            raise Exception("Wrong play parameters!")

        user.save()

        serializer = userProfileSerializer(user)
        # TODO add validation
        # serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)

        return JsonResponse(serializer.data, safe=False)

#
class UserAddFriend(UpdateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def put(self, request, *args, **kwargs):

        try:
            friend_name = request.query_params.get('name')
        except:
            Exception("Cannot befriend...?")

        try:
            friend = userProfile.objects.get(user__username=friend_name)
        except:
            Exception("No such user?")
        usr = userProfile.objects.get(user=request.user)
        usr.friends.add(friend)

        usr.save()

        serializer = userProfileSerializer(usr)
        # TODO add validation
        # serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)

        return JsonResponse(serializer.data, safe=False)


class UserProfileListCreateView(ListCreateAPIView):
    search_fields = ["user__username"]
    filter_backends = (filters.SearchFilter,)
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
