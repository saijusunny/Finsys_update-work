# Generated by Django 4.0.4 on 2022-11-21 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_item_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_stock',
            name='bitm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasebill'),
        ),
    ]
