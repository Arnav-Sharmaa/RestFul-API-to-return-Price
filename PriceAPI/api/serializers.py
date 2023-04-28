from rest_framework import serializers
from .models import element

class elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = element
        fields = '__all__'