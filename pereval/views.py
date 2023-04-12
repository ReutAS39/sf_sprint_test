from rest_framework import generics

from pereval.models import PerevalAdded
from sf_sprint.serializers import PerevalSerializer



class PerevalApiView(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer
