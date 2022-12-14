# Generated by Django 4.0.2 on 2022-12-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_vendor_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='banking_payment',
            fields=[
                ('bnkpymid', models.AutoField(primary_key=True, serialize=False, verbose_name='BNK_PYM_ID')),
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
                ('paid_through', models.CharField(max_length=100)),
                ('ref_no', models.CharField(max_length=100, null=True)),
                ('account', models.CharField(max_length=100, null=True)),
                ('expenseaccount', models.CharField(max_length=100, null=True)),
                ('reference', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='expense_banking',
            name='accounts1id',
        ),
        migrations.RemoveField(
            model_name='expense_banking',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='vendor_payment',
            name='accounts1id',
        ),
        migrations.RemoveField(
            model_name='vendor_payment',
            name='cid',
        ),
        migrations.DeleteModel(
            name='customer_payment',
        ),
        migrations.DeleteModel(
            name='expense_banking',
        ),
        migrations.DeleteModel(
            name='vendor_payment',
        ),
    ]
