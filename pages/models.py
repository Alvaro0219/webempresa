from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'

    def __str__(self):
        return self.title
