# Generated by Django 3.2.2 on 2021-06-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0005_alter_neighbourhood_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]