# import local data
# Create your views here.
# Create  a viewset
from .serializers import GeeksSerializer
from rest_framework import viewsets
from .models import GeeksModel


class GeekViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = GeeksModel.object.all()

    # specify serializer to be used
    serializer_class = GeeksSerializer
