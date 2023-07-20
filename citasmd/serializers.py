from django.contrib.auth.models import User, Group
from citasmd.models import CitasMd, Doctor, Especialidad, Paciente
from rest_framework import serializers


class CitasMdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CitasMd
        fields = ['fecha_cita', 'activo', 'doctor', 'paciente']

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id_doctor', 'Doc_nomb', 'Doc_Apellido', 'Doc_direccion', 'especialidad']

class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['nom_especialidad', 'activo']

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id_paciente', 'Pac_nomb', 'Pac_Apellido', 'Pac_edad', 'correo']