from django.shortcuts import render
from django.views.generic import ListView
from .models import Bolete

class BoleteListView(ListView):
    model = Bolete
    template_name = 'bolete_list.html'