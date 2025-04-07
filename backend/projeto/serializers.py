from rest_framework import serializers
from .models import Viagem

class ViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viagem
        fields = '__all__'