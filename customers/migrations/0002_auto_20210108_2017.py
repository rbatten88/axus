# Generated by Django 3.1.4 on 2021-01-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalemail',
            name='email',
            field=models.EmailField(blank=True, max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='additionalphone',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
