# Generated by Django 5.1 on 2024-09-04 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=70)),
                ('marks', models.IntegerField()),
                ('passdate', models.DateField()),
                ('admdatetime', models.DateTimeField()),
            ],
        ),
    ]
