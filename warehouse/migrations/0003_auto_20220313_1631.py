# Generated by Django 3.1.4 on 2022-03-13 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20220313_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.inventory'),
        ),
    ]