# Generated by Django 2.2.6 on 2019-10-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rango', '0004_auto_20191009_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]