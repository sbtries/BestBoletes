from rest_framework import generics
from boletes.models import Bolete
from .serializers import BoleteSerializer

class BoleteAPIView(generics.ListAPIView):
    queryset = Bolete.objects.all()
    serializer_class = BoleteSerializer