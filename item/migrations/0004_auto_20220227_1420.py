# Generated by Django 3.1.4 on 2022-02-27 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_group_itemgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemgroup',
            old_name='ited_id',
            new_name='item_id',
        ),
    ]
