# Generated by Django 5.0.4 on 2024-05-14 04:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TransPorto', '0005_rutas_id_unidad_unidadtransporte_detalles_de_ruta'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaladministrativo',
            name='id_unidad',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='TransPorto.unidadtransporte'),
            preserve_default=False,
        ),
    ]
