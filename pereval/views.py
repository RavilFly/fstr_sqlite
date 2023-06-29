from django.shortcuts import render
from rest_framework import generics
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer

class SubmitData(generics. ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
