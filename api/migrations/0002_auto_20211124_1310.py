# Generated by Django 3.1.2 on 2021-11-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammodel',
            name='logo',
            field=models.URLField(verbose_name='Team Logo'),
        ),
    ]