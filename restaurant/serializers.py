from rest_framework import serializers
from .models import Menu, Booking_table


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_table
        fields = '__all__'

