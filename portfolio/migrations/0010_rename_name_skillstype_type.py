# Generated by Django 4.0.5 on 2022-09-04 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_remove_skills_type_skills_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillstype',
            old_name='name',
            new_name='type',
        ),
    ]