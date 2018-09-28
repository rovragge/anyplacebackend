# Generated by Django 2.1.1 on 2018-09-26 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AnyPlaceRest', '0008_auto_20180926_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='navi_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AnyPlaceRest.NaviAddress'),
        ),
        migrations.AlterField(
            model_name='user',
            name='navi_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AnyPlaceRest.NaviAddress'),
        ),
    ]
