from django.contrib import admin
from .models import Editora


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ['editora',]
    search_fields = ['editora', 'telefone']
