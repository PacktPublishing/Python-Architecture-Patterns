from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Micropost, Usr
from .serializers import MicropostSerializer

import logging

logger = logging.getLogger(__name__)


class MicropostsListView(ListCreateAPIView):
    serializer_class = MicropostSerializer

    def get_queryset(self):
        logger.info('Getting queryset')
        result = Micropost.objects.filter(user__username=self.kwargs['username'])
        logger.info(f'Querysert ready {result}')
        return result

    def perform_create(self, serializer):
        user = Usr.objects.get(username=self.kwargs['username'])
        serializer.save(user=user)


class MicropostView(RetrieveUpdateDestroyAPIView):
    serializer_class = MicropostSerializer

    def get_queryset(self):
        logger.info('Getting queryset for single element')
        result = Micropost.objects.filter(user__username=self.kwargs['username'])
        logger.info(f'Queryset ready {result}')
        return result
