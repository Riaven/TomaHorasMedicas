# Generated by Django 2.2.7 on 2019-11-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_auto_20191121_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
