# Generated by Django 4.1.2 on 2022-12-03 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('department', models.CharField(max_length=50)),
                ('code', models.TextField()),
                ('section', models.TextField()),
                ('units', models.TextField()),
                ('timetable', models.TextField()),
                ('location', models.TextField()),
                ('instructor', models.TextField()),
                ('course_dates', models.TextField()),
                ('status', models.TextField()),
                ('capacity', models.TextField()),
                ('description', models.TextField(default='N/A')),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
