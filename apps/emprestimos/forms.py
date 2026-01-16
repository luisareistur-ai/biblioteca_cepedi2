from django import forms
from django.forms import ModelForm, DateInput

from apps.emprestimos.models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        exclude = ('data_emprestimo',)
        fields = '__all__'
<<<<<<< HEAD
        widgets = {
        'data_devolucao': forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={'type': 'date'}
        ),

        'data_prevista_devolucao': forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={'type': 'date'}
        ),
}
=======

        widgets = {
            'data_devolucao': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione uma data',
                       'type': 'date'  
                       }),
            'data_prevista_devolucao': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Selecione uma data',
                       'type': 'date' 
                       }),
        }
>>>>>>> dec613af3560ee40193b9f197de6e822329538d0
