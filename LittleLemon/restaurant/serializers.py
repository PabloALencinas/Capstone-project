from rest_framework import serializers
from .models import Booking, Menu
from django.contrib.auth.models import User, Group

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = ['id','title','price','inventory']
        

        
