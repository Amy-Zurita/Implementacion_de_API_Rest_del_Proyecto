from citasmd.models import CitasMd
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CitasMd
        fields = ['fecha_cita', 'activo']


