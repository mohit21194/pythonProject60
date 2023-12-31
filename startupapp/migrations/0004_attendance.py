# Generated by Django 4.1.7 on 2023-06-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupapp', '0003_payments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.CharField(max_length=50)),
                ('logintime', models.CharField(max_length=50)),
                ('logouttime', models.CharField(max_length=50)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
