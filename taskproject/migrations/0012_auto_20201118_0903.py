# Generated by Django 3.1.3 on 2020-11-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskproject', '0011_auto_20201118_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='arq',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]