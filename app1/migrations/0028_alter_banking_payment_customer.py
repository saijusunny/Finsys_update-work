# Generated by Django 4.0.2 on 2022-12-09 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_banking_payment_pym_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banking_payment',
            name='customer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
