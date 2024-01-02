# Generated by Django 5.0 on 2024-01-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrateur'), ('teacher', 'Enseignant')], default='admin', max_length=50),
        ),
    ]