# Generated by Django 3.2.4 on 2021-06-19 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20210619_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.order'),
        ),
    ]
