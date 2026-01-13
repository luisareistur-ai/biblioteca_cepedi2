from django.db import models


class Editora(models.Model):
    editora = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.editora

    class Meta:
        db_table = 'Editora'
        verbose_name = 'Editora'
        ordering = ['editora']


from django.db import models

# Create your models here.
