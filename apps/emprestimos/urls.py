from django.urls import path
from apps.emprestimos import views

app_name = 'apps.emprestimos'

urlpatterns = [
    path('inserir_emprestimo', views.inserir_emprestimo, name='inserir_emprestimo'),
]