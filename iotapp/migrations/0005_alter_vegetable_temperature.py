# Generated by Django 4.1.3 on 2023-02-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotapp', '0004_vegetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegetable',
            name='temperature',
            field=models.CharField(max_length=10),
        ),
    ]
