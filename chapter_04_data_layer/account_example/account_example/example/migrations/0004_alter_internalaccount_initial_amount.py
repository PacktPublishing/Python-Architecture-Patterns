# Generated by Django 3.2 on 2021-05-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_internalaccount_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internalaccount',
            name='initial_amount',
            field=models.IntegerField(default=1),
        ),
    ]
