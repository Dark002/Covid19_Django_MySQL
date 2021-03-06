# Generated by Django 3.0.7 on 2020-10-30 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='world',
            name='continent',
        ),
        migrations.AlterField(
            model_name='india_statewise',
            name='state_name',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='country_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='date',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
