# Generated by Django 4.0.2 on 2022-12-07 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_rename_debit_no_salescreditnote_credit_no_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='vendor_payment',
        ),
    ]