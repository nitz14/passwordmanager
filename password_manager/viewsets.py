from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Servises
from .serializers import ServisesSerializer


class ServisesViewSet(viewsets.ModelViewSet):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = ServisesSerializer
    queryset = Servises.objects.all()

    def get_queryset(self):
        queryset = Servises.objects.all()
        servises_id = self.request.query_params.get('id')
        if servises_id:
            queryset = Servises.objects.filter(id=servises_id)
        return queryset
