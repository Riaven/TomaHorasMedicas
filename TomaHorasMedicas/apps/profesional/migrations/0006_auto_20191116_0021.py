# Generated by Django 2.2.7 on 2019-11-16 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesional', '0005_auto_20191113_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='foto',
            field=models.ImageField(upload_to='images/profesionales/'),
        ),
    ]