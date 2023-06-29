from django.urls import path
from .views import SubmitData, UpdateSubmitData

urlpatterns = [
    path('submitdata/', SubmitData.as_view()),
    path('submitdata/<int:pk>/', UpdateSubmitData.as_view()),
]