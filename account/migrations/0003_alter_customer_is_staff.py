# Generated by Django 4.0.2 on 2022-05-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customer_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]