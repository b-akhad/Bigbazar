# Generated by Django 3.2.6 on 2021-08-21 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0014_alter_user_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 21, 9, 12, 38, 359758)),
        ),
    ]