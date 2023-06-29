from django.urls import path
from .views import SubmitData

urlpatterns = [
    path('submitdata/', SubmitData.as_view()),
]