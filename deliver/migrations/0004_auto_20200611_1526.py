# Generated by Django 3.0.3 on 2020-06-11 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliver', '0003_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='telephone',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]
