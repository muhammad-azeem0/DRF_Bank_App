# Generated by Django 5.0.1 on 2024-02-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='default_accounting_type',
            field=models.CharField(max_length=6),
        ),
    ]
