from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListAPIView
from pereval.models import PerevalAdded, Users
from pereval.serializers import PerevalSerializer#, PerevalSubmitDataListSerializer


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
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin):

    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    def get_queryset(self):
        email = self.request.query_params.get('user__email', None)
        pk = self.kwargs.get('pk')
        if email:
            return self.queryset.filter(user__email=email)
        elif pk:
            return self.queryset.filter(id=pk)
        return self.queryset.none()
    # def perform_create(self, serializer):
    #     serializer.save()

# class SubmitDataUpdateView(UpdateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = PerevalUpdateSerializer
#
    def update(self, request, *args, **kwargs):
        submit_data = self.get_object()


        if submit_data.status != 'new':
            return Response({'state': 0, 'message': 'Данные не могут быть отредактированы'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(submit_data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'state': 1, 'message': 'Данные успешно отредактированы'})

# class SubmitDataListView(ListAPIView):
#     queryset = PerevalAdded.objects.all()
#     serializer_class = PerevalSerializer
#
#     def get_queryset(self):
#         email = self.request.query_params.get('user__email', None)
#         if email is not None:
#             return self.queryset.filter(user__email=email)
#         return self.queryset.none()