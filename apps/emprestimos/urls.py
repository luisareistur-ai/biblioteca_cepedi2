from django.urls import path
<<<<<<< HEAD
from apps.emprestimos import views
=======
from . import views

>>>>>>> dec613af3560ee40193b9f197de6e822329538d0

app_name = 'apps.emprestimos'

urlpatterns = [
<<<<<<< HEAD
    path('inserir_emprestimo', views.inserir_emprestimo, name='inserir_emprestimo'),
    path('listar_emprestimos', views.listar_emprestimos, name='listar_emprestimos'),
    path('editar_emprestimo/<int:id>', views.editar_emprestimo, name='editar_emprestimo'),
    path('excluir_emprestimo/<int:id>', views.excluir_emprestimo, name='excluir_emprestimo'),
]
=======
    path('inserir_emprestimo/', views.inserir_emprestimo, name='inserir_emprestimo'),
    path('listar_emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
]
>>>>>>> dec613af3560ee40193b9f197de6e822329538d0
