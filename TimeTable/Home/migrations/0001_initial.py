# Generated by Django 5.0.3 on 2024-03-14 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=35)),
                ('teacher_desig', models.CharField(max_length=15)),
                ('subjects', models.CharField(max_length=150)),
            ],
        ),
    ]
