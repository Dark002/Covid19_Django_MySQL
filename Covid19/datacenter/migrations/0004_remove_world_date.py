# Generated by Django 3.0.7 on 2020-10-31 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0003_auto_20201030_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='world',
            name='date',
        ),
    ]