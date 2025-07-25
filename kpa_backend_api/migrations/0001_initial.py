# Generated by Django 5.2.4 on 2025-07-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WheelSpecificationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_number', models.CharField(max_length=50, unique=True)),
                ('submitted_by', models.CharField(max_length=100)),
                ('submitted_date', models.DateField()),
                ('fields', models.JSONField()),
                ('status', models.CharField(default='Saved', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
