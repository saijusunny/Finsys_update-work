# Generated by Django 4.0.2 on 2022-11-28 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_remove_purchasebill_item_itmdt'),
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
        migrations.CreateModel(
            name='expense_banking',
            fields=[
                ('expenseid', models.AutoField(primary_key=True, serialize=False, verbose_name='exid')),
                ('date', models.DateField(null=True)),
                ('expenseaccount', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('vendor', models.CharField(max_length=100, null=True)),
                ('customer', models.CharField(max_length=100, null=True)),
                ('reference', models.CharField(max_length=100, null=True)),
                ('note', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(default='default.png', upload_to='purchase/expense')),
                ('running_bal', models.CharField(max_length=100)),
                ('accounts1id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.accounts1')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='customer_payment',
            fields=[
                ('customerpymid', models.AutoField(primary_key=True, serialize=False, verbose_name='CUSTPYMID')),
                ('customer', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100, null=True)),
                ('amount_received', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('received_through', models.CharField(max_length=100)),
                ('paym_ref_no', models.CharField(max_length=100)),
                ('bnk_ref_no', models.CharField(max_length=100)),
                ('file', models.FileField(default='default.jpg', upload_to='Customer')),
                ('des', models.CharField(max_length=100, null=True)),
                ('running_bal', models.CharField(max_length=100)),
                ('accounts1id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.accounts1')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
