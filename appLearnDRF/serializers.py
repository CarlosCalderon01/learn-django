from rest_framework import serializers
from .models import *

class UserClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClientModel
        fields = '__all__'

