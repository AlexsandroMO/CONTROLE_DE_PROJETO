# Generated by Django 3.1.3 on 2020-11-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskproject', '0007_cotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotation',
            name='qt_doc',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='cotation',
            name='qt_page',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]