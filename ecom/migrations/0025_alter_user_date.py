# Generated by Django 3.2.6 on 2021-08-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0024_alter_user_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
