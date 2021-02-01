# Generated by Django 3.1.4 on 2021-02-01 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_type', models.CharField(choices=[('', ''), ('Delivery', 'Delivery'), ('Pickup', 'Pickup'), ('TBD', 'TBD')], default='', max_length=8)),
                ('transfer_date', models.DateField(blank=True, null=True)),
                ('transfer_time', models.CharField(choices=[('', ''), ('AM', 'AM'), ('PM', 'PM'), ('Anytime', 'Anytime'), ('8am-10am', '8am-10am'), ('10am-12pm', '10am-12pm'), ('12pm-2pm', '12pm-2pm'), ('2pm-4pm', '2pm-4pm'), ('First Drop', 'First Drop')], default='', max_length=20)),
                ('status', models.CharField(choices=[('Order', 'Order'), ('Confirmed', 'Confirmed'), ('Load Matched', 'Load Matched'), ('Invoice Made', 'Invoice Made'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Settled', 'Settled'), ('Completed', 'Completed')], default='Order', max_length=20)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.wholesalecustomer')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
            ],
        ),
    ]
