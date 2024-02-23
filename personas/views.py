#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from personas.forms import PersonaForm
from personas.models import Persona
from personas.tasks import send_mail_persona_update_task
from my_deploy.celery import debug_task


# Create your views here.
class PersonaList(ListView):
    model = Persona
    template_name = "personas/personas_list.html"
    ordering = ['id']


class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "personas/personas_create.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'La persona se ha creado exitosamente.')
        return super().form_valid(form)


class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/personas_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'La persona se ha editado exitosamente.')
        send_mail_persona_update_task.delay()
        return super().form_valid(form)


class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'personas/personas_delete.html'
    success_url = reverse_lazy('index')
