# Generated by Django 5.1.4 on 2025-01-13 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250, verbose_name='Code')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('type', models.IntegerField(verbose_name='Type')),
                ('sub_type', models.IntegerField(default=0, verbose_name='Sub Type')),
                ('order_no', models.IntegerField(default=1, verbose_name='Order Number')),
                ('info1', models.IntegerField(default=0, verbose_name='Info1')),
                ('info2', models.IntegerField(default=0, verbose_name='Info2')),
                ('info3', models.IntegerField(default=0, verbose_name='Info3')),
                ('info4', models.IntegerField(default=0, verbose_name='Info4')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='pub.parameters', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Parameter',
                'verbose_name_plural': 'Parameters',
            },
        ),
    ]