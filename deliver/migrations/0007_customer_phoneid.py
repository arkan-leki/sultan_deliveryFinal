# Generated by Django 3.0.3 on 2020-06-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliver', '0006_customer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phoneid',
            field=models.CharField(default='Unknown', max_length=110),
        ),
    ]
