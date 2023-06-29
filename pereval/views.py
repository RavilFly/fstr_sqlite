from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import PerevalAdded, Users
from .serializers import PerevalAddedSerializer, UserPerevalSerializer

class SubmitData(generics. ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def post(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Отправлено успешно',
                'id': serializer.data['id'],
            })
        elif status.HTTP_400_BAD_REQUEST:
            return Response({
                    'status': 400,
                    'message': 'Ошибка в запросе, проверьте поля.',
                    'id': None,
                })
        elif status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': 500,
                'message': 'Ошибка при выполнении операции.',
                'id': None,
            })

        else:
            return self.create(request, *args, **kwargs)

class UpdateSubmitData(generics.RetrieveUpdateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PATCH not allowed"})

        try:
            instance = PerevalAdded.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        if instance.status == 'new':
            serializer = PerevalAddedSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'state': '1', 'message': "Запись обновлена"})

        else:
            return Response({'state': '0', 'message':'Изменять можно только сообщения со статусом "new"'})

class UserPerevalList(generics.ListAPIView):
    serializer_class = UserPerevalSerializer

    def get_queryset(self):
        user = Users.objects.filter(email=self.kwargs['email'])[0]
        queryset = PerevalAdded.objects.filter(user__email=user.email)

        return queryset

