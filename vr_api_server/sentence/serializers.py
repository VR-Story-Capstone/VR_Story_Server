# chat /serializers.py
from rest_framework import serializers
from .models import Sentence

class SentenceSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(allow_blank=True)
    complement = serializers.CharField(allow_blank=True)
    object = serializers.CharField(allow_blank=True)
    modifier = serializers.CharField(allow_blank=True)
    predicate = serializers.CharField(allow_blank=True)

    class Meta:
        model = Sentence
        fields = '__all__'
