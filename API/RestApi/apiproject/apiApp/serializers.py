
from rest_framework import serializers
from apiApp.models import *

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'