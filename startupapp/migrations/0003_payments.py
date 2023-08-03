# Generated by Django 4.1.7 on 2023-06-16 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startupapp', '0002_trainer_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountPaid', models.IntegerField()),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(default='Unpaid', max_length=20)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startupapp.register')),
            ],
        ),
    ]
