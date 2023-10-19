# Generated by Django 4.2.6 on 2023-10-17 09:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='The Phone number is not correct', regex='^/d{10}$')])),
                ('Query', models.TextField()),
                ('Query_date', models.DateTimeField()),
            ],
        ),
    ]