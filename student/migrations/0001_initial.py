# Generated by Django 4.1.2 on 2022-12-04 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolled_courses_of_a_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('professor_id', models.IntegerField()),
                ('student_id', models.IntegerField()),
                ('grade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=200)),
                ('major', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
