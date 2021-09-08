from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from ecom.models import *
from django.contrib import messages


def home(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Product.objects.filter(brand__icontains=search).order_by("-id")
    else:
        products = Product.objects.order_by("-id")
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'home.html', {'products': products})


def shoe_link(request):
    if 'search' in request.GET:
        search = request.GET['search']
        shoes = Shoe.objects.filter(brand__icontains=search).order_by("-id")
    else:
        shoes = Shoe.objects.order_by("-id")
    paginator = Paginator(shoes, 12)
    page = request.GET.get('page')
    shoes = paginator.get_page(page)
    return render(request, 'shoes.html', {'shoes': shoes})


def dress_link(request):
    if 'search' in request.GET:
        search = request.GET['search']
        dresses = Dress.objects.filter(brand__icontains=search).order_by("-id")
    else:
        dresses = Dress.objects.order_by("-id")
    paginator = Paginator(dresses, 12)
    page = request.GET.get('page')
    dresses = paginator.get_page(page)
    return render(request, 'dresses.html', {'dress': dresses})


def bags_link(request):
    if 'search' in request.GET:
        search = request.GET['search']
        bags = Bag.objects.filter(brand__icontains=search).order_by("-id")
    else:
        bags = Bag.objects.order_by("-id")
    paginator = Paginator(bags, 12)
    page = request.GET.get('page')
    bags = paginator.get_page(page)
    return render(request, 'bags.html', {'bags': bags})


def treasure_link(request):
    if 'search' in request.GET:
        search = request.GET['search']
        treasure = Treasure.objects.filter(brand__icontains=search).order_by("-id")
    else:
        treasure = Treasure.objects.order_by("-id")
    paginator = Paginator(treasure, 12)
    page = request.GET.get('page')
    treasure = paginator.get_page(page)
    return render(request, 'treasure.html', {'treasure': treasure})


def hijab_link(request):
    if 'search' in request.GET:
        search = request.GET['search']
        hijab = Hijab.objects.filter(brand__icontains=search).order_by("-id")
    else:
        hijab = Hijab.objects.order_by("-id")
    paginator = Paginator(hijab, 12)
    page = request.GET.get('page')
    hijab = paginator.get_page(page)
    return render(request, 'hijab.html', {'hijab': hijab})


def romol_link(request):
    if 'search' in request.GET:
        search = request.GET['search']
        romol = Romol.objects.filter(brand__icontains=search).order_by("-id")
    else:
        romol = Romol.objects.order_by("-id")
    paginator = Paginator(romol, 12)
    page = request.GET.get('page')
    romol = paginator.get_page(page)
    return render(request, 'Romol.html', {'romol': romol})





def detail(request, pk):
    product = Product.objects.get(pk=pk)
    content = {"product": product}
    if request.method == 'POST':
        if request.POST.get('ism') and request.POST.get('telefon'):
            save = User()
            save.first_name = request.POST.get('ism')
            save.phone = request.POST.get('telefon')
            save.product_id = product
            save.save()
            messages.success(request, "Sizga tez orada qo'ng'iroq qilamiz ")
            return render(request, "details.html", content)

    return render(request, "details.html", content)


def sh_detail(request, pk):
    shoe = Shoe.objects.get(pk=pk)
    content = {"shoe": shoe}
    if request.method == 'POST':
        if request.POST.get('ism') and request.POST.get('telefon'):
            save = User()
            save.first_name = request.POST.get('ism')
            save.phone = request.POST.get('telefon')
            save.product_id = shoe
            save.save()
            messages.success(request, "Sizga tez orada qo'ng'iroq qilamiz ")
            return render(request, "sh-detail.html", content)

    return render(request, "sh-detail.html", content)


def d_detail(request, pk):
    dresses = Dress.objects.get(pk=pk)
    content = {"dresses": dresses}
    if request.method == 'POST':
        if request.POST.get('ism') and request.POST.get('telefon'):
            save = User()
            save.first_name = request.POST.get('ism')
            save.phone = request.POST.get('telefon')
            save.product_id = dresses
            save.save()
            messages.success(request, "Sizga tez orada qo'ng'iroq qilamiz")
            return render(request, "d-detail.html", content)

    return render(request, "d-detail.html", content)


def b_detail(request, pk):
    bags = Bag.objects.get(pk=pk)
    content = {"bags": bags}
    if request.method == 'POST':
        if request.POST.get('ism') and request.POST.get('telefon'):
            save = User()
            save.first_name = request.POST.get('ism')
            save.phone = request.POST.get('telefon')
            save.product_id = bags
            save.save()
            messages.success(request, "Sizga tez orada qo'ng'iroq qilamiz")
            return render(request, "b-detail.html", content)

    return render(request, "b-detail.html", content)


def t_detail(request, pk):
    treasure = Treasure.objects.get(pk=pk)
    content = {"treasure": treasure}
    if request.method == 'POST':
        if request.POST.get('ism') and request.POST.get('telefon'):
            save = User()
            save.first_name = request.POST.get('ism')
            save.phone = request.POST.get('telefon')
            save.product_id = treasure
            save.save()
            messages.success(request, "Sizga tez orada qo'ng'iroq qilamiz")
            return render(request, "t-detail.html", content)

    return render(request, "t-detail.html", content)


def h_detail(request, pk):
    hijab = Hijab.objects.get(pk=pk)
    content = {"hijab": hijab}
    if request.method == 'POST':
        if request.POST.get('ism') and request.POST.get('telefon'):
            save = User()
            save.first_name = request.POST.get('ism')
            save.phone = request.POST.get('telefon')
            save.product_id = hijab
            save.save()
            messages.success(request, "Sizga tez orada qo'ng'iroq qilamiz")
            return render(request, "h-detail.html", content)

    return render(request, "h-detail.html", content)


def romol_detail(request, pk):
    romol = Romol.objects.get(pk=pk)
    content = {"romol": romol}
    if request.method == 'POST':
        if request.POST.get('ism') and request.POST.get('telefon'):
            save = User()
            save.first_name = request.POST.get('ism')
            save.phone = request.POST.get('telefon')
            save.product_id = romol
            save.save()
            messages.success(request, "Sizga tez orada qo'ng'iroq qilamiz")
            return render(request, "detail-r.html", content)

    return render(request, "detail-r.html", content)


