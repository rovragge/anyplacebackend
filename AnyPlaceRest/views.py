import json
from django.http import JsonResponse, HttpResponse
from AnyPlaceRest.models import *
from AnyPlaceRest import serializers
from AnyPlaceRest.naviaddress_api import NaviAddressApi


# Create your views here.

def get_local_image(request, path):
    with open(path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


def upload_image_navi(request):
    file = request.FILES['image'].file
    api = NaviAddressApi()
    result, status = api.upload_image(file)
    return JsonResponse({'result': result}, status=status)


def categories_get(request):
    categories = Category.objects.all()
    return JsonResponse({'result': serializers.category_serialize(categories)}, status=200)


def place_create(request):
    body = json.loads(request.body)
    title = body.get('title')
    description = body.get('description')
    address = body.get('address')
    phone = body.get('phone')
    if title is None or description is None or address is None or phone is None:
        return JsonResponse({}, status=400)

    place = Place(
        title=title,
        description=description,
        address=address,
        phone=phone,
    )
    place.save()
    return JsonResponse({'result': serializers.place_serialize(place)}, status=200)


def place_info(request, place):
    place = Place.objects.filter(pk=place).first()
    if place is None:
        return JsonResponse({}, status=404)
    if request.method == 'GET':
        return JsonResponse({'result': serializers.place_serialize(place.id)}, status=200)
    return JsonResponse({}, status=415)


def place_categories_edit(request, place):
    place = Place.objects.filter(pk=place).first()
    if place is None:
        return JsonResponse({}, status=404)
    if request.method == 'GET':
        return JsonResponse({'result': serializers.category_serialize(place.categories.all())}, status=200)
    if request.method == 'POST':
        body = json.loads(request.body)
        categories = body['categories']
        cats = Category.objects.filter(pk__in=categories).all()
        place.categories.add(*cats)
        place.save()
        return JsonResponse({}, status=200)
    if request.method == 'DELETE':
        body = json.loads(request.body)
        categories = body['categories']
        cats = Category.objects.filter(pk__in=categories).all()
        place.categories.remove(*cats)
        place.save()
        return JsonResponse({}, status=200)


def place_get_orders(request, place):
    place = Place.objects.filter(pk=place).first()
    if place is None:
        return JsonResponse({}, status=404)
    status = request.GET.get('status')
    orders = Order.objects.filter(place_id=place.id)
    if status is not None:
        orders = orders.filter(status=status)
    return JsonResponse({'result': serializers.order_serialize(orders)}, status=200)


def place_naviaddrss_edit(request, place):
    place = Place.objects.filter(pk=place).first()
    if place is None:
        return JsonResponse({}, status=404)
    navi = place.navi_address
    api = NaviAddressApi()
    if request.method == 'GET':
        if navi is not None:
            result = api.get_naviaddress(navi.container, navi.naviaddress)
            return JsonResponse({'result': result}, status=200)
        return JsonResponse({}, status=404)
    if request.method == 'POST':
        body = json.loads(request.body)
        lat = float(body.get('lat'))
        lng = float(body.get('lng'))
        map_visibility = body.get('map_visibility')
        cover = body.get('cover')
        if navi is None:
            if lat is None or lng is None:
                return JsonResponse({}, status=400)
            navi_json, status = api.create_naviaddress(lat=lat, lng=lng)
            if status != 200:
                return JsonResponse({'result': 'NaviAddress API Error'}, status=500)
            container = navi_json['container']
            naviaddress = navi_json['naviaddress']
            navi_json, status = api.confirm_naviaddress(container=container, naviaddress=naviaddress)
            if status != 200:
                return JsonResponse({'result': 'NaviAddress API Error'}, status=500)
            navi_json, status = api.update_naviaddress(container=container, naviaddress=naviaddress,
                                                       name=place.title, description=place.description)
            if status != 200:
                return JsonResponse({'result': 'NaviAddress API Error'}, status=500)
            navi = NaviAddress(container=container, naviaddress=naviaddress, name=place.title)
            navi.save()
            place.navi_address = navi
            place.save()
            return JsonResponse({'result': api.get_naviaddress(navi.container, navi.naviaddress)}, status=200)
        else:
            api.update_naviaddress(container=navi.container, naviaddress=navi.naviaddress,
                                   name=place.title, description=place.description,
                                   lat=lat, lng=lng, cover=cover, map_visibility=map_visibility,)
            return JsonResponse({'result': api.get_naviaddress(navi.container, navi.naviaddress)}, status=200)
    if request.method == 'DELETE':
        if navi is None:
            return JsonResponse({'result': 'You cant delete your NaviAddress cause you do not have it, lol'})
        result, status = api.delete_naviaddress(container=navi.container, naviaddress=navi.naviaddress)
        if status == 200:
            navi.delete()
            return JsonResponse({'result': result}, status=200)
        return JsonResponse({'result': 'NaviAddress API Error'}, status=500)


def user_register(request):
    body = json.loads(request.body)
    login = body['login']
    password = body['password']

    if User.objects.filter(login=login).exists():
        return JsonResponse({}, status=409)
    else:
        User(login=login, password=password).save()
        return JsonResponse({}, status=200)


def user_update(request):
    token = int(request.META.get('HTTP_X_AUTH_TOKEN'))
    user = User.objects.filter(pk=token).first()
    if user is None:
        return JsonResponse({}, status=401)
    body = json.loads(request.body)
    if body.get('fio') is not None:
        user.fio = body['fio']
    if body.get('phone') is not None:
        user.phone = body['phone']
    if body.get('passport') is not None:
        user.passport = body['passport']
    if body.get('send_frequency') is not None:
        user.send_frequency = body['send_frequency']

    user.save()
    return JsonResponse({'result': serializers.user_serialize(user.id)}, status=200)


def user_passport_upload(request):
    token = int(request.META.get('HTTP_X_AUTH_TOKEN'))
    user = User.objects.filter(pk=token).first()
    if user is None:
        return JsonResponse({}, status=401)
    file = request.FILES['image']
    user.passport_photo = file
    user.save()
    return JsonResponse({'result': serializers.user_serialize(user.id)}, status=200)


def user_login(request):
    body = json.loads(request.body)
    login = body.get('login')
    password = body.get('password')
    if login is None or password is None:
        return JsonResponse({}, status=400)
    user = User.objects.filter(login=login, password=password)
    res = serializers.user_serialize(user)
    return JsonResponse({'result': res}, status=200 if res is not None else 401)


def user_whoami(request):
    token = int(request.META.get('HTTP_X_AUTH_TOKEN'))
    user = User.objects.filter(pk=token)
    res = serializers.user_serialize(user)
    return JsonResponse({'result': res}, status=200 if res is not None else 401)


def user_get_orders_seller(request):
    token = int(request.META.get('HTTP_X_AUTH_TOKEN'))
    orders = Order.objects.filter(seller_id=token)
    return JsonResponse({'result': serializers.order_serialize(orders)})


def user_update_naviaddress(request):
    token = int(request.META.get('HTTP_X_AUTH_TOKEN'))
    user = User.objects.filter(pk=token).first()
    navi = user.navi_address
    api = NaviAddressApi()

    if request.method == 'GET':
        if navi is not None:
            result = api.get_naviaddress(navi.container, navi.naviaddress)
            return JsonResponse({'result': result}, status=200)
        return JsonResponse({}, status=404)

    if request.method == 'POST':
        body = json.loads(request.body)
        lat = float(body.get('lat'))
        lng = float(body.get('lng'))

        if navi is None:
            if lat is None or lng is None:
                return JsonResponse({}, status=400)
            navi_json, status = api.create_naviaddress(lat=lat, lng=lng)
            if status != 200:
                return JsonResponse({'result': 'NaviAddress API Error'}, status=500)
            container = navi_json['container']
            naviaddress = navi_json['naviaddress']
            navi_json, status = api.confirm_naviaddress(container=container, naviaddress=naviaddress)
            if status != 200:
                return JsonResponse({'result': 'NaviAddress API Error'}, status=500)
            navi_json, status = api.update_naviaddress(container=container, naviaddress=naviaddress, name=user.login)
            if status != 200:
                return JsonResponse({'result': 'NaviAddress API Error'}, status=500)
            navi = NaviAddress(container=container, naviaddress=naviaddress, name=user.login)
            navi.save()
            user.navi_address = navi
            user.save()
            return JsonResponse({'result': api.get_naviaddress(navi.container, navi.naviaddress)}, status=200)
        else:

            api.update_naviaddress(container=navi.container, naviaddress=navi.naviaddress, name=navi.name,
                                   lat=lat, lng=lng)
            return JsonResponse({'result': api.get_naviaddress(navi.container, navi.naviaddress)}, status=200)
