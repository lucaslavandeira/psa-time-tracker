# Generated by Django 2.1 on 2018-11-17 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0007_remove_taskassignment_hours_spent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskwork',
            name='date',
            field=models.DateField(),
        ),
    ]
