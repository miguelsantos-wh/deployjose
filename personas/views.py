#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from personas.forms import PersonaForm
from personas.models import Persona


# Create your views here.
class PersonaList(ListView):
    model = Persona
    template_name = "personas/personas_list.html"


class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "personas/personas_create.html"
    success_url = reverse_lazy('index')


class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/personas_create.html'
    success_url = reverse_lazy('index')


class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'personas/personas_delete.html'
    success_url = reverse_lazy('index')
