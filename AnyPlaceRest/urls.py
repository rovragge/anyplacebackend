from django.urls import path, re_path

from AnyPlaceRest import views

urlpatterns = [
    re_path(r'^image/(?P<path>.*)$', views.get_local_image),  # GET
    path('upload_image', views.upload_image_navi),  # POST

    path('user/login', views.user_login),  # POST
    path('user/update', views.user_update),  # POST
    path('user/register', views.user_register),  # POST
    path('user/whoami', views.user_whoami),  # GET
    path('user/orders', views.user_get_orders),  # GET
    path('user/order/create', views.user_create_order),  # POST
    path('user/naviaddress', views.user_update_naviaddress),  # POST
    path('user/passport', views.user_passport_upload),  # POST

    path('categories', views.categories_get),  # GET

    path('place/create', views.place_create),  # POST
    path('place/<place>', views.place_info),  # POST
    path('place/<place>/categories', views.place_categories_edit),
    path('place/<place>/naviaddress', views.place_naviaddrss_edit),
    path('place/<place>/orders', views.place_get_orders),

]
