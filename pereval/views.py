from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from pereval.models import PerevalAdded
from sf_sprint.serializers import PerevalSerializer



class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer


class SubmitData(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass