# Generated by Django 2.2.7 on 2019-11-07 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('contenido', models.CharField(max_length=300)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
