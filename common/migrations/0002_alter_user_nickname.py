# Generated by Django 4.0.3 on 2023-01-11 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]