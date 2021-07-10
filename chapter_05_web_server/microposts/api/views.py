from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Micropost, Usr
from .serializers import MicropostSerializer


class MicropostsListView(ListCreateAPIView):
    serializer_class = MicropostSerializer

    def get_queryset(self):
        return Micropost.objects.filter(user__username=self.kwargs['username'])

    def perform_create(self, serializer):
        user = Usr.objects.get(username=self.kwargs['username'])
        serializer.save(user=user)


class MicropostView(RetrieveUpdateDestroyAPIView):
    serializer_class = MicropostSerializer

    def get_queryset(self):
        return Micropost.objects.filter(user__username=self.kwargs['username'])
