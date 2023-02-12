from django.forms import ModelForm
from .models import CERTIFICATE,downloadcertificate
from django import forms
class CertificateForm(ModelForm):
    class Meta:
        model = CERTIFICATE
        fields = ['name' , 'address' , 'hospitalName', 'date', 'doctorName', 'ticketid']

class downloadForm(ModelForm):
    class Meta:
        model = downloadcertificate
        fields = ['name', 'slip_id']

