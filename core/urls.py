from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('cashier_pos/', views.cashier_pos, name='cashier_pos'),
    path('login/', views.user_login, name='user_login'),
    path('inventory_management/', views.inventory_management, name='inventory_management'),
    path('sales_report/', views.sales_report, name='sales_report'),
    path('add_item/', views.add_item, name='add_item'),
    path('category_management/', views.category_management, name='category_management'),
    path('user_management/', views.user_management, name='user_management'),
    path('logout/', views.logout_view, name='logout'),
    path('add_item/', views.add_item, name='add_item'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('item_autocomplete/', views.item_autocomplete, name='item_autocomplete'),
    path('cashier_pos/', views.cashier_pos, name='cashier_pos'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('search_item/<str:item_name>/', views.search_item, name='search_item'),
    path('ajax/live-search/', views.live_search_items, name='live_search_items'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_inventory/<int:item_id>/', views.update_inventory, name='update_inventory'),
    path('record_sale/', views.record_sale, name='record_sale'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('suppliers/<int:pk>/edit/', views.supplier_update, name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.supplier_confirm_delete, name='supplier_confirm_delete'),
    path('stock_card/<int:item_id>/', views.stock_card, name='stock_card'),
    path('search_items/', views.search_items, name='search_items'),

]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
