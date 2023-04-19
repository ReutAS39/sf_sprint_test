from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListAPIView
from pereval.models import PerevalAdded, Users
from pereval.serializers import PerevalSerializer


# class PerevalViewSet(viewsets.ModelViewSet):
#     queryset = PerevalAdded.objects.all()
#     serializer_class = PerevalSerializer


# class submitData(mixins.CreateModelMixin, viewsets.GenericViewSet): # ok
#     queryset = PerevalAdded.objects.all()
#     serializer_class = PerevalSerializer

# class submitData(viewsets.GenericViewSet, mixins.ListModelMixin):
#     queryset = PerevalAdded.objects.all()
#     serializer_class = PerevalSerializer
#
#     def create(self, request, *args, **kwargs):
#         #print(request.data['user']['email']) адрес
#         #print(Users.objects.filter(email=request.data['user']['email']).exists())   наличие его в бд
#
#         serializer = self.get_serializer(data=request.data)
#         #print(request.data.pop('user')['email'])
#         #print(request.data)
#         serializer.is_valid(raise_exception=True)
#         #print(serializer.validated_data)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#     def get_success_headers(self, data):
#         try:
#             return {'Location': str(data[api_settings.URL_FIELD_NAME])}
#         except (TypeError, KeyError):
#             return {}


class submitData(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet,
                 mixins.UpdateModelMixin):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    def update(self, request, *args, **kwargs):
        submit_data = self.get_object()
        print(submit_data)


        if submit_data.status != 'new':
            message = 'Данные не могут быть отредактированы, т.к. статус "new" не соответствует.'
            return Response({'state': 0, 'message': message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(submit_data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'state': 1})


# class SubmitDataUpdateView(UpdateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = PerevalUpdateSerializer
#
#     def update(self, request, *args, **kwargs):
#         submit_data = self.get_object()
#
#
#         if submit_data.status != 'new':
#             message = 'Данные не могут быть отредактированы, т.к. статус "new" не соответствует.'
#             return Response({'state': 0, 'message': message}, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = self.get_serializer(submit_data, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         return Response({'state': 1})