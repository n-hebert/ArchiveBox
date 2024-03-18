# Generated by Django 3.1.14 on 2024-01-24 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaults', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archiveboxdefaultdependency',
            options={'verbose_name': 'Default Configuration: Dependencies'},
        ),
        migrations.AlterModelOptions(
            name='archiveboxdefaultextractor',
            options={'verbose_name': 'Default Configuration: Extractors'},
        ),
        migrations.AlterField(
            model_name='archiveboxdefaultdependency',
            name='BINARY',
            field=models.CharField(default='/bin/bash', max_length=255),
        ),
        migrations.AlterField(
            model_name='archiveboxdefaultdependency',
            name='ENABLED',
            field=models.BooleanField(default=True),
        ),
    ]