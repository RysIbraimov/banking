from django.shortcuts import render
from django.views import generic
from .models import Client

class ClientViews(generic.ListView):
    model = Client
    context_object_name = 'clients'
    template_name = 'clients.html'

class DetailClientView(generic.DetailView):
    model = Client
    context_object_name = 'client'
    template_name = 'detail.html'
