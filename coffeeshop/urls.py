from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('<int:menu_id>/', views.detail, name='detail'),
    path('<int:menu_id>/order/', views.order, name='order'),
    path('total_order/', views.total_order, name='total_order'),
    path('group_order_type/', views.group_order_type, name='group_order_type'),
    path('<int:type_id>/group_order_result/', views.group_order_result, name='group_order_result'),
    path('group_order_size/', views.group_order_size, name='group_order_size'),
    path('<slug:size_type>/group_order_size_result/', views.group_order_size_result, name='group_order_size_result')
]