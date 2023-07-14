from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from citasmd.models import CitasMd
from rest_framework import viewsets, permissions
from webapp.serializers import UserSerializer


def mostrar_citasmd(request):
    cantidad_citasmd = CitasMd.objects.count()
    pagina = loader.get_template('citasmd.html')
    lista_citasmds =  CitasMd.objects.all()
    datos = {'cantidad':cantidad_citasmd, 'citasmds':lista_citasmds}
    return HttpResponse(pagina.render(datos, request))


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CitasMd.objects.all().order_by('paciente')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]