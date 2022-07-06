from rest_framework import serializers
from  .models import *

class Trainers(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        fields='__all__'
