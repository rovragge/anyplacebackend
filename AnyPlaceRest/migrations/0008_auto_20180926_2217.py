# Generated by Django 2.1.1 on 2018-09-26 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnyPlaceRest', '0007_auto_20180926_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naviaddress',
            name='address_type',
        ),
        migrations.RemoveField(
            model_name='naviaddress',
            name='default_lang',
        ),
        migrations.RemoveField(
            model_name='naviaddress',
            name='description',
        ),
        migrations.RemoveField(
            model_name='naviaddress',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='naviaddress',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='naviaddress',
            name='map_visibility',
        ),
        migrations.RemoveField(
            model_name='naviaddress',
            name='postal_address',
        ),
    ]
