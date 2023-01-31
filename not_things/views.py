from rest_framework import generics
from .models import Not_Thing
from .serializers import Not_ThingSerializer
# Create your views here.


class Not_ThingList(generics.ListCreateAPIView):
    queryset = Not_Thing.objects.all()
    serializer_class = Not_ThingSerializer

class Not_ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Not_Thing.objects.all()
    serializer_class = Not_ThingSerializer