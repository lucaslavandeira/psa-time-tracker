# Generated by Django 2.1 on 2018-10-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='assigned_projects',
            field=models.ManyToManyField(blank=True, to='tracking.Task'),
        ),
    ]