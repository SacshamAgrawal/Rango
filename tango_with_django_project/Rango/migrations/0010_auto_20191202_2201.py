# Generated by Django 2.2.6 on 2019-12-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rango', '0009_auto_20191202_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
