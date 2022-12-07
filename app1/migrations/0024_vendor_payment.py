# Generated by Django 4.0.2 on 2022-12-07 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_delete_vendor_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendor_payment',
            fields=[
                ('vendorpymid', models.AutoField(primary_key=True, serialize=False, verbose_name='CUSTPYMID')),
                ('vendor', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=100, null=True)),
                ('amount_received', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('paid_through', models.CharField(max_length=100)),
                ('ref_no', models.CharField(max_length=100, null=True)),
                ('account', models.CharField(max_length=100, null=True)),
                ('des', models.CharField(max_length=100, null=True)),
                ('running_bal', models.CharField(max_length=100)),
                ('accounts1id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.accounts1')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
