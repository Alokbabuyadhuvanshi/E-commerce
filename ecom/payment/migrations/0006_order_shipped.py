# Generated by Django 5.1.1 on 2025-02-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
