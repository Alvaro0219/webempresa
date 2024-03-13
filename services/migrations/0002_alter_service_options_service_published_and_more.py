# Generated by Django 5.0.2 on 2024-03-07 14:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AddField(
            model_name='service',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='service',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualizado'),
        ),
    ]
