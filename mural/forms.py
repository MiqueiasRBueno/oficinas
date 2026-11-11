from django import forms
from .models import Recado


class RecadoForm(forms.ModelForm):
    class Meta:
        model = Recado
        fields = ["nome", "email"]
