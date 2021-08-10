from django.urls import path
from .views import BoleteAPIView

urlpatterns = [
path('', BoleteAPIView.as_view()),
]