# Generated by Django 4.2.6 on 2023-11-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='crear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100, verbose_name='usuario')),
                ('contraseña', models.CharField(max_length=100, verbose_name='contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='detallar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compra', models.CharField(max_length=100, verbose_name='compra')),
                ('detalles_envio', models.TextField(verbose_name='Mensaje')),
            ],
        ),
    ]
