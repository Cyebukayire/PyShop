# Generated by Django 2.2.20 on 2021-08-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
