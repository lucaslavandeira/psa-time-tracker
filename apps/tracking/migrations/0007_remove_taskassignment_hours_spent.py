# Generated by Django 2.1 on 2018-11-16 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0006_taskwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskassignment',
            name='hours_spent',
        ),
    ]
