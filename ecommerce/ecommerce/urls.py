from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import user_login, user_logout, product_list, add_to_cart, view_cart, place_order, product_detail, add_product, edit_product, delete_product,
product_list, search_products, filter_products, category_list, tag_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='авторизоваться'),
    path('logout/', user_logout, name='выход'),
    path('', product_list, name='список товаров'),
    path('add_to_cart//', add_to_cart, name='добавить в корзину'),
    path('cart/', view_cart, name='просмотреть корзину'),
    path('place_order/', place_order, name='заказать'),
    path('product//', product_detail, name='product_detail'),
    path('product/add/', add_product, name='add_product'),
    path('product/edit//', edit_product, name='edit_product'),
    path('product/delete//', delete_product, name='delete_product'),
    path('search/', search_products, name='search_products'),
    path('filter/', filter_products, name='filter_products'),
    path('category/', category_list, name='category_list'),
    path('tag/', tag_list, name='tag_list'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)