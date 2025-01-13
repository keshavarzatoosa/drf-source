# Generated by Django 5.1.4 on 2025-01-13 14:48

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('manager_name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=blog.models.Bank._select_bank_type, max_length=12)),
                ('status', models.CharField(choices=blog.models.Bank._select_status, max_length=12)),
                ('address', models.CharField(max_length=250)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(choices=blog.models.Person._select_status, max_length=12),
        ),
    ]