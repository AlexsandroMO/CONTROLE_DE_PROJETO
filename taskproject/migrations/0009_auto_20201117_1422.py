# Generated by Django 3.1.3 on 2020-11-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskproject', '0008_auto_20201115_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotation',
            name='cost_doc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='cotation',
            name='cost_hh',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='cotation',
            name='qt_hh',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
    ]
