# Generated by Django 3.0.3 on 2020-06-22 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deliver', '0014_auto_20200622_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bnkauser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BnkasUser', to=settings.AUTH_USER_MODEL),
        ),
    ]