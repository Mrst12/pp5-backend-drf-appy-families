# Generated by Django 3.2.15 on 2022-09-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='urgent',
            field=models.BooleanField(blank=True),
        ),
    ]
