# Generated by Django 2.0.2 on 2018-03-16 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
