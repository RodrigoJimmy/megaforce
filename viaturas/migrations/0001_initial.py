# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Marca ou fabricante', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Modelo da viatura', max_length=100, unique=True)),
                ('foto', models.ImageField(blank=True, help_text='Foto da viatura', null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('marca', models.ForeignKey(help_text='Marca da viatura', on_delete=django.db.models.deletion.CASCADE, to='viaturas.Marca')),
            ],
            options={
                'verbose_name_plural': 'Modelos',
                'ordering': ['nome'],
                'get_latest_by': 'updated_at',
            },
        ),
    ]
