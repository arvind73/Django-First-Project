# Generated by Django 3.1.4 on 2021-01-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0002_auto_20210102_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]