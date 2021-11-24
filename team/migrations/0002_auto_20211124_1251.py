# Generated by Django 3.1.2 on 2021-11-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.URLField(max_length=255, verbose_name='Avatar URL'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.URLField(max_length=255, verbose_name='Logo URL'),
        ),
    ]