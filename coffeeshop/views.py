from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum, F, Count
from django.db import models

from .models import Type, Menu, Orders

def index(request):
    return render(request, 'coffeeshop/index.html')

def menu(request):
    all_menu = Menu.objects.order_by('menu_type')
    context = {'all_menu': all_menu}
    return render(request, 'coffeeshop/menu.html', context)

def detail(request, menu_id):
    detail_menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'coffeeshop/detail.html', {'detail_menu':detail_menu})

def total_order(request):
    all_order = Orders.objects.order_by('-order_date').values('menu', 'order', 'order_date', 'menu__menu_text', 'menu__size_text', 'menu__price').annotate(total=Sum(F('order') * F('menu__price'), output_field=models.FloatField()))
    total_order = Orders.objects.aggregate(total=Sum(F('order') * F('menu__price'), output_field=models.FloatField()))['total']
    context = {'all_order':all_order,'total_order':total_order}
    return render(request, 'coffeeshop/total_order.html', context)

def group_order_type(request):
    menu_type = Type.objects.all()
    context = {'menu_type':menu_type}
    return render(request, 'coffeeshop/group_order_type.html', context)

def group_order_result(request, type_id):
    order_result = Orders.objects.filter(menu__menu_type=type_id).values('menu', 'order', 'order_date', 'menu__menu_text', 'menu__size_text', 'menu__price').order_by('-order_date').annotate(total=Sum(F('order') * F('menu__price'), output_field=models.FloatField()))
    total_order = Orders.objects.aggregate(total=Sum(F('order') * F('menu__price'), output_field=models.FloatField()))['total']
    context = {'order_result':order_result,'total_order':total_order}
    return render(request, 'coffeeshop/group_order_result.html', context)

def group_order_size(request):
    all_size = Menu.objects.values_list('size_text', flat=True).distinct()
    context = {'all_size':all_size}
    return render(request, 'coffeeshop/group_order_size.html', context)

def group_order_size_result(request, size_type):
    order_result = Orders.objects.filter(menu__size_text__contains=size_type).values('menu', 'order', 'order_date', 'menu__menu_text', 'menu__size_text', 'menu__price').order_by('-order_date').annotate(total=Sum(F('order') * F('menu__price'), output_field=models.FloatField()))
    total_order = Orders.objects.aggregate(total=Sum(F('order') * F('menu__price'), output_field=models.FloatField()))['total']
    context = {'order_result':order_result,'total_order':total_order}
    return render(request, 'coffeeshop/group_order_size_result.html', context)

def order(request, menu_id):
    quantity = request.POST['quantity']
    if quantity is None or quantity <= '0':
        detail_menu = get_object_or_404(Menu, pk=menu_id)
        return render(request, 'coffeeshop/detail.html',{
            'detail_menu':detail_menu,
            'error_message':'You did not put order.', 
        })
    else:
        menu = Menu.objects.get(id=menu_id)
        order = Orders(menu=menu, order=quantity)
        order.save()
        return HttpResponseRedirect(reverse('index'))