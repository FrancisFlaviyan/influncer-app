from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import AllData
from .serializers import AllDataSerializer

class AllDataViewSet(viewsets.ModelViewSet):
    queryset = AllData.objects.all()
    serializer_class = AllDataSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message": "Saved Successfully"})
        return Response(serializer.errors)
