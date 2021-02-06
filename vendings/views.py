# local Django
from .serializers import *

# third party
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class VendingListView(generics.ListAPIView):
    queryset = Vending.objects.all()
    serializer_class = VendingSerializer
    permission_classes = [AllowAny]


class VendingBuyView(APIView):
    queryset = Vending.objects.all()
    serializer_class = VendingBuySerializer

    def post(self, request):
        try:
            vend = Vending.objects.get(id_key=request.data['id_key'])
        except(vend.DoesNotExist):
            return Response({"error": "Vending not found"}, status=status.HTTP_404_NOT_FOUND)
        if vend is not None:
            vend.count -= int(request.data['update'])
            vend.total_sum += int(request.data['update'])
            vend.save()
            return Response({"message": "Vending machine has been updated."}, status=status.HTTP_200_OK)


class VendingFillView(APIView):
    queryset = Vending.objects.all()
    serializer_class = VendingFillSerializer

    def post(self, request):
        try:
            vend = Vending.objects.get(id_key=request.data['id_key'])
        except(vend.DoesNotExist):
            return Response({"error": "Vending not found"}, status=status.HTTP_404_NOT_FOUND)
        if vend is not None:
            vend.count += int(request.data['update'])
            vend.save()
            return Response({"message": "Vending machine has been updated."}, status=status.HTTP_200_OK)


class VendingEmptyListView(generics.ListAPIView):
    queryset = Vending.objects.filter(count=0)
    serializer_class = VendingSerializer