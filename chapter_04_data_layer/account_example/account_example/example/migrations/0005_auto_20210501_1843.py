# Generated by Django 3.2 on 2021-05-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_alter_internalaccount_initial_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalaccount',
            name='branch_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='internalaccount',
            name='initial_amount',
            field=models.IntegerField(default=0),
        ),
    ]
