# Generated by Django 3.1.2 on 2021-11-23 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='team')),
                ('description', models.CharField(default='', max_length=255, verbose_name='Team Descriptions')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, unique=True)),
                ('avatar', models.ImageField(upload_to='member')),
                ('description', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(default='', unique=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='team.team', verbose_name='Team')),
            ],
        ),
    ]