from django.conf.urls import url, include
from personas.views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete

urlpatterns = [
    url(r'create/', PersonaCreate.as_view(), name="persona_create"),
    url(r'update/(?P<pk>\d+)/', PersonaUpdate.as_view(), name="persona_update"),
    url(r'delete/(?P<pk>\d+)/', PersonaDelete.as_view(), name="persona_delete"),
    url(r'^$', PersonaList.as_view(), name="index"),
]
