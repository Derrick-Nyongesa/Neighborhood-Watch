# Generated by Django 3.2.2 on 2021-06-04 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0008_alter_business_neighbourhood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='price',
        ),
    ]
