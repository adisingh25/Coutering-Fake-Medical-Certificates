from django.forms import ModelForm
from .models import CERTIFICATE

class CertificateForm(ModelForm):
    class Meta:
        model = CERTIFICATE
        fields = ['name' , 'address' , 'hospitalName', 'date', 'doctorName']


