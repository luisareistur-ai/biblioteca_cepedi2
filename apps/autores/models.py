from django.db import models


class Autor(models.Model):
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.autor

    class Meta:
        db_table = 'Autor'
        verbose_name = 'Autor'
        ordering = ['autor']
