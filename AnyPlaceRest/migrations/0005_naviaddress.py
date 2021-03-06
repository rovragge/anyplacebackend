# Generated by Django 2.1.1 on 2018-09-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnyPlaceRest', '0004_user_send_frequency'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaviAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container', models.CharField(default='', max_length=255, verbose_name='container')),
                ('naviaddress', models.CharField(default='', max_length=255, verbose_name='naviaddress')),
                ('address_type', models.CharField(default='', max_length=255, verbose_name='')),
                ('lat', models.FloatField(default='', max_length=255, verbose_name='lat')),
                ('lng', models.FloatField(default='', max_length=255, verbose_name='lng')),
                ('postal_address', models.CharField(default='', max_length=255, verbose_name='postal_address')),
                ('map_visibility', models.BooleanField(default=True, verbose_name='map_visibility')),
            ],
        ),
    ]
