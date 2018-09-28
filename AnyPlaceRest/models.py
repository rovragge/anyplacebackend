from django.db import models


# Create your models here.

class NaviAddress(models.Model):
    container = models.CharField(verbose_name='container', max_length=255, default="")
    naviaddress = models.CharField(verbose_name='naviaddress', max_length=255, default="")
    name = models.CharField(verbose_name='name', max_length=255, default="", null=True)


class User(models.Model):
    login = models.CharField(verbose_name='login', max_length=255, default="", unique=True)
    password = models.CharField(verbose_name='password', max_length=255, default="")
    fio = models.CharField(verbose_name='fio', max_length=255, default="",null=True)
    phone = models.CharField(verbose_name='phone', max_length=255, default="", null=True)
    passport = models.CharField(verbose_name='passport', max_length=255, default="", null=True)
    passport_photo = models.ImageField(verbose_name='passport_photo', upload_to='AnyPlaceRest/passport_photos', null=True)
    send_frequency = models.IntegerField(verbose_name='send_frequency', default=0)
    navi_address = models.ForeignKey(NaviAddress, on_delete=models.SET_NULL, null=True)


class Category(models.Model):
    name = models.CharField(verbose_name='name', max_length=255, default="")
    description = models.CharField(verbose_name='description', max_length=1000, default="", null=True)


class Place(models.Model):
    title = models.CharField(verbose_name='title', max_length=255, default="")
    description = models.CharField(verbose_name='description', max_length=1000, default="", null=True)
    address = models.CharField(verbose_name='title', max_length=255, default="")
    phone = models.CharField(verbose_name='title', max_length=255, default="")
    categories = models.ManyToManyField(Category)
    navi_address = models.ForeignKey(NaviAddress, on_delete=models.SET_NULL, null=True)


class Order(models.Model):
    seller = models.ForeignKey(User, related_name='seller_id', on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(User, related_name='buyer_id', on_delete=models.DO_NOTHING)
    place = models.ForeignKey(Place, related_name='place_id', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name='category_id', on_delete=models.DO_NOTHING)
    product = models.CharField(verbose_name='product', max_length=255, default="")
    product_url = models.CharField(verbose_name='product_url', max_length=255, default="")
    acceptance_date = models.DateTimeField(verbose_name='acceptance_date', auto_now=True)
    delivery_date = models.DateTimeField(verbose_name='delivery_date', auto_now=True)
    status = models.IntegerField(verbose_name='status', default=0)
    price = models.FloatField(verbose_name='price', default=0.0)

