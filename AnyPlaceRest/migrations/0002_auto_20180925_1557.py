# Generated by Django 2.1.1 on 2018-09-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnyPlaceRest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='navi_address',
            field=models.IntegerField(default=0, null=True, verbose_name='navi_address'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='description'),
        ),
    ]
