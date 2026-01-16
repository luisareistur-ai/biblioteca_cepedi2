from django import forms
from apps.autores.models import Autor


class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = '__all__'