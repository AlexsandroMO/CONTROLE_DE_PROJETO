# Generated by Django 3.1.3 on 2020-12-04 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(max_length=12)),
                ('created_st', models.DateTimeField(auto_now_add=True)),
                ('update_st', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_doc', models.CharField(max_length=3)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('update_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=255)),
                ('emp_office', models.CharField(max_length=255)),
                ('emp_contrato', models.CharField(max_length=20)),
                ('created_emp', models.DateTimeField(auto_now_add=True)),
                ('update_emp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('comments', models.TextField()),
                ('created_proj', models.DateTimeField(auto_now_add=True)),
                ('update_proj', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pageformat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_format', models.CharField(max_length=15)),
                ('created_fm', models.DateTimeField(auto_now_add=True)),
                ('update_fm', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_page', models.CharField(max_length=3)),
                ('created_pt', models.DateTimeField(auto_now_add=True)),
                ('update_pt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_by_hh', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('cost_by_doc', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('cost_by_A1', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_status', models.CharField(max_length=50)),
                ('created_st', models.DateTimeField(auto_now_add=True)),
                ('update_st', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=255)),
                ('created_sub', models.DateTimeField(auto_now_add=True)),
                ('update_sub', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arq', models.FileField(upload_to='uploads/')),
                ('update_arq', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documment_name', models.CharField(max_length=255)),
                ('created_doc', models.DateTimeField(auto_now_add=True)),
                ('update_doc', models.DateTimeField(auto_now=True)),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskproject.doct')),
                ('doc_type_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskproject.paget')),
                ('format_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskproject.pageformat')),
            ],
        ),
        migrations.CreateModel(
            name='Cotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(blank=True, max_length=255, null=True)),
                ('qt_page', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('qt_hh', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('cost_doc', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('created_ct', models.DateTimeField(auto_now_add=True)),
                ('update_ct', models.DateTimeField(auto_now=True)),
                ('cod_doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskproject.doct')),
                ('doc_name_pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskproject.documentstandard')),
                ('format_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskproject.pageformat')),
                ('page_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskproject.paget')),
                ('proj_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskproject.myproject')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskproject.subject')),
            ],
        ),
    ]
