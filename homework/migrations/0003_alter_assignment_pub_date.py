# Generated by Django 3.2 on 2022-01-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_auto_20220119_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
