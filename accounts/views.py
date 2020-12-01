from django.http import JsonResponse
from rest_framework.generics import UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


from .models import userProfile, mapPlay
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer, mapPlaySerializer

from rest_framework import filters



class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class UserOwnProfile(RetrieveUpdateDestroyAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfileOrReadOnly, ]

    def get_object(self, queryset=None):
        user = userProfile.objects.get(user=self.request.user)
        return self.queryset.get(pk=user.id)

    def get(self, request, *args, **kwargs):
        user = userProfile.objects.get(user=request.user)
        serializer = userProfileSerializer(user)
        return JsonResponse(serializer.data, safe=False)


class UserOwnPlays(ListCreateAPIView):
    queryset = mapPlay.objects.all()
    serializer_class = mapPlaySerializer
    search_fields = ["user"]
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAuthenticated, IsOwnerProfileOrReadOnly, ]

    def get_object(self, queryset=mapPlay.objects.all()):
        user = userProfile.objects.get(user=self.request.user)
        return self.queryset.get(user=user.id)

    # def get(self, request, *args, **kwargs):
    #     user = userProfile.objects.get(user=request.user)
    #     serializer = userProfileSerializer(user)
    #     return JsonResponse(serializer.data, safe=False)

class UserPlay(UpdateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        # print(request.user) is just the name
        user = userProfile.objects.get(user=request.user)
        user.map_plays += 1


        try:
            length = float(request.query_params.get('length'))
            score = int(request.query_params.get('score'))
            mapid = request.query_params.get('mapid')
        except:
            raise Exception("Wrong play parameters!")

        mapPlay.objects.create(mapid=mapid, score=score, user=user)
        user.hours_played += length / 3600
        user.total_score += score

        if request.query_params.get('passed') == "true":
            user.successful_map_plays += 1

        user.save()
        serializer = userProfileSerializer(user)

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


        friend = userProfile.objects.get(user__username=friend_name)
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

