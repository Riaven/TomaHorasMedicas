# Generated by Django 2.2.7 on 2019-11-13 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesional', '0003_auto_20191112_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='sector',
            field=models.CharField(choices=[('R', 'ROJO'), ('A', 'AZUL')], max_length=15),
        ),
    ]
