from django.contrib import messages
from django.shortcuts import render

from ecom.models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from ecom.models import *


def searching(func,model=Product):
    def wrapper(request, *args, **kwargs):
        if 'search' in request.GET:
            search = request.GET['search']
            products = model.objects.filter(brand__icontains=search).order_by("-id")
        else:
            products = model.objects.order_by("-id")
            paginator = Paginator(products, 12)
            page = request.GET.get('page')
            products = paginator.get_page(page)
        return func(request, *args, **kwargs)
    return wrapper


def search(request, model):
    if 'search' in request.GET:
        search = request.GET['search']
        products = model.objects.filter(brand__icontains=search).order_by("-id")
    else:
        products = model.objects.order_by("-id")
        paginator = Paginator(products, 12)
        page = request.GET.get('page')
        products = paginator.get_page(page)
    return products


def order(request, product:object):
    if request.POST.get('ism') and request.POST.get('telefon'):
        save = User()
        save.first_name = request.POST.get('ism')
        save.phone = request.POST.get('telefon')
        save.product_id = product
        save.save()
        messages.success(request, "Sizga tez orada qo'ng'iroq qilamiz ")

