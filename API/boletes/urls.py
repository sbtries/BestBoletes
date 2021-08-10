from django.urls import path
from .views import BoleteListView

urlpatterns = [
    path('', BoleteListView.as_view(), name='home'),
]