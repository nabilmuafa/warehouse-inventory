from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, \
    show_json_by_id, show_xml_by_id, register, login_user, logout_user, \
    decrement, increment, delete, get_json_by_user, add_items_ajax, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('create-item/', create_item, name="create_item"),
    path('create-flutter/', create_product_flutter,
         name="create_product_flutter"),
    path('delete/', delete, name="delete"),
    path('dec/', decrement, name="dec"),
    path('inc/', increment, name="inc"),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name="show_json"),
    path('create-ajax/', add_items_ajax, name="add_items_ajax"),
    path('user-json/', get_json_by_user, name="get-json-by-user"),
    path('xml/<int:id>/', show_xml_by_id, name="show_xml_by_id"),
    path('json/<int:id>/', show_json_by_id, name="show_json_by_id")
]
