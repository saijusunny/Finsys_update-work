# Generated by Django 4.0.2 on 2022-12-03 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_alter_customer_city_alter_customer_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountype',
            name='accountname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]