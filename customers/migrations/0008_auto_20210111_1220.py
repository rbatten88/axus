# Generated by Django 3.1.4 on 2021-01-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20210111_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesalecustomer',
            name='current_balance',
            field=models.IntegerField(default='0'),
        ),
    ]
