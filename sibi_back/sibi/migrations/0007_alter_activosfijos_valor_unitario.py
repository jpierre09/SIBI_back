# Generated by Django 4.2.4 on 2023-08-05 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibi', '0006_alter_activosfijos_numero_contrato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activosfijos',
            name='valor_unitario',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
