from django import forms
from apps.editoras.models import Editora


class EditoraForm(forms.ModelForm):

    class Meta:
        model = Editora
        fields = '__all__'