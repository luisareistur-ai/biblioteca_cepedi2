from django.contrib import admin
from .models import Autor


@admin.register(Autor)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ['autor',]
    search_fields = ['autor',]
