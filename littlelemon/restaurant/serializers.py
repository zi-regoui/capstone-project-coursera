from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Booking

# class BookingSerializer(ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']