# Generated by Django 3.1.4 on 2022-03-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_auto_20220313_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
