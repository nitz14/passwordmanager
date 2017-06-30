from rest_framework import serializers
from .models import Servises


class ServisesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servises
        fields = ('id', 'page_name', 'page_url', 'user', 'password')
