# Generated by Django 5.0 on 2023-12-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_school_adress_alter_school_sigle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.EmailField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
