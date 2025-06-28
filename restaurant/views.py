from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Booking_table, Menu
from .serializers import bookingSerializer, menuSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')



class BookingviewSet(ModelViewSet):
    queryset = Booking_table.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated]


class Menuview(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This is protected"})