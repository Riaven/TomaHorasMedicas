# Generated by Django 2.2.7 on 2019-11-13 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesional', '0002_profesional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='foto',
            field=models.ImageField(upload_to='static/images/profesionales/'),
        ),
    ]
