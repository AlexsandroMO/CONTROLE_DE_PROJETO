# Generated by Django 3.1.3 on 2020-11-18 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskproject', '0010_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='update_ct',
            new_name='update_arq',
        ),
    ]
