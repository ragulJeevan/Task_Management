from rest_framework import serializers
from .models import Status,Type,Stage,Complexity,Priority,Sdlc

# Status 
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

# TYPE 
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
# STAGE 
class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'
# COMPLEXITY 
class ComplexitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Complexity
        fields = '__all__'
# PRIORITY 
class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'
# SDLC 
class SdlcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sdlc
        fields = '__all__'