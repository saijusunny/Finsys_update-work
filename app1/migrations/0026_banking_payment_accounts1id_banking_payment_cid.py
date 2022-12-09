# Generated by Django 4.0.2 on 2022-12-09 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_banking_payment_remove_expense_banking_accounts1id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banking_payment',
            name='accounts1id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.accounts1'),
        ),
        migrations.AddField(
            model_name='banking_payment',
            name='cid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.company'),
            preserve_default=False,
        ),
    ]