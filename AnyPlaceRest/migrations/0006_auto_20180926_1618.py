# Generated by Django 2.1.1 on 2018-09-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnyPlaceRest', '0005_naviaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='naviaddress',
            name='default_lang',
            field=models.CharField(default='', max_length=255, verbose_name='default_lang'),
        ),
        migrations.AlterField(
            model_name='naviaddress',
            name='address_type',
            field=models.CharField(default='', max_length=255, verbose_name='address_type'),
        ),
    ]
