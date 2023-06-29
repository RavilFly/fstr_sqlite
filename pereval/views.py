from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer

class SubmitData(generics. ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def post(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': None,
                'id': serializer.data['id'],
            })
        elif status.HTTP_400_BAD_REQUEST:
            return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Ошибка в запросе, проверьте поля.',
                    'id': None,
                })

        else:
            return self.create(request, *args, **kwargs)
