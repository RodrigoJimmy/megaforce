# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viaturas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=8)),
                ('prefixo', models.CharField(max_length=8)),
                ('status', models.CharField(choices=[('d', 'Disponível'), ('b', 'Baixada'), ('m', 'Manutenção')], default='d', help_text='Situação da viatura', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('modelo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viaturas.Modelo')),
            ],
            options={
                'ordering': ['prefixo'],
            },
        ),
        migrations.AlterField(
            model_name='marca',
            name='nome',
            field=models.CharField(help_text='Marca ou fabricante (ex.: Ford, GM, Volkswagen, ...)', max_length=100, unique=True),
        ),
    ]