from AnyPlaceRest.models import *


def user_serialize(user):
    fields = ['id', 'login', 'phone', 'passport', 'passport_photo', 'navi_address_id', 'send_frequency']
    if user is None:
        return None
    if isinstance(user, int):
        user = list(User.objects.filter(id=user).values())
    else:
        user = list(user.values(*fields))
    for o in user:
        o['navi_address_id'] = naviaddress_serialize(o['navi_address_id'])
    if len(user) == 0:
        return None
    elif len(user) == 1:
        return user[0]
    else:
        return user


def place_serialize(place):
    if isinstance(place, int):
        place = list(Place.objects.filter(id=place).values())
    else:
        place = list(place.values())
    for o in place:
        o['navi_address_id'] = naviaddress_serialize(o['navi_address_id'])
    if len(place) == 0:
        return None
    elif len(place) == 1:
        return place[0]
    else:
        return place


def category_serialize(category):
    if isinstance(category, int):
        category = list(Category.objects.filter(id=category).values())
    else:
        category = list(category.values())
    if len(category) == 0:
        return None
    elif len(category) == 1:
        return category[0]
    else:
        return category


def naviaddress_serialize(navi_address):
    if navi_address is None:
        return None
    elif isinstance(navi_address, int):
        navi_address = list(NaviAddress.objects.filter(id=navi_address).values())
    else:
        navi_address = list(navi_address.values())
    if len(navi_address) == 0:
        return None
    elif len(navi_address) == 1:
        return navi_address[0]
    else:
        return navi_address


def order_serialize(order):
    if isinstance(order, int):
        order = list(Order.objects.filter(id=order).values())
    else:
        order = list(order.values())

    for o in order:
        o['seller_id'] = user_serialize(o['seller_id'])
        o['buyer_id'] = user_serialize(o['buyer_id'])
        o['place_id'] = place_serialize(o['place_id'])
        o['category_id'] = category_serialize(o['category_id'])
        o['acceptance_date'] = o['acceptance_date'].timestamp()
        o['delivery_date'] = o['delivery_date'].timestamp()

    return order
