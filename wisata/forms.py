from django.forms import ModelForm
from django import forms
from .models import *

class FormWisata(ModelForm):
    class Meta:
        model = Wisata
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'harga_tiket' : forms.TextInput({'class':'form-control'}),
            'penginapan' : forms.TextInput({'class':'form-control'}),
            'tipe_id' : forms.Select({'class':'form-control'}),
            'keterangan' : forms.TextInput({'class':'form-control'})
        }