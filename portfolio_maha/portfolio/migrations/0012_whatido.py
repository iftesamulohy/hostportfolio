# Generated by Django 4.0.5 on 2022-09-04 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_iconcolor'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatIdo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('icon', models.CharField(max_length=15)),
                ('color_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.iconcolor')),
            ],
        ),
    ]
