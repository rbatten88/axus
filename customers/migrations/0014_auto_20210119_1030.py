# Generated by Django 3.1.4 on 2021-01-19 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_auto_20210117_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalemail',
            old_name='email',
            new_name='add_email',
        ),
        migrations.RenameField(
            model_name='additionalphone',
            old_name='phone_number',
            new_name='add_phone_number',
        ),
    ]
