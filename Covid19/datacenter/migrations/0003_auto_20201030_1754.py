# Generated by Django 3.0.7 on 2020-10-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0002_auto_20201030_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='world',
            name='date',
            field=models.DateField(null=True),
        ),
    ]