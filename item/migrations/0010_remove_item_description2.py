# Generated by Django 3.1.4 on 2022-05-10 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_item_description2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description2',
        ),
    ]
