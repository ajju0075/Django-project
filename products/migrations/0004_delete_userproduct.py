# Generated by Django 4.1.4 on 2022-12-15 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_userproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProduct',
        ),
    ]