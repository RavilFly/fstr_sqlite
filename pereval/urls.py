from django.urls import path
from .views import SubmitData, UpdateSubmitData, UserPerevalList

urlpatterns = [
    path('submitdata/', SubmitData.as_view()),
    path('submitdata/<int:pk>/', UpdateSubmitData.as_view()),
    path('submitdata/user__email=<str:email>/', UserPerevalList.as_view()),
]