from django.shortcuts import render

# Create your views here.
from ecom.models import *
from ecom.decorators import search, order


def home(request):
    return render(request, 'home.html', {'products': search(request, Product)})


def shoe_link(request):
    return render(request, 'shoes.html', {'shoes': search(request, Shoe)})


def dress_link(request):
    return render(request, 'dresses.html', {'dress': search(request, Dress)})


def bags_link(request):
    return render(request, 'bags.html', {'bags': search(request, Bag)})


def treasure_link(request):
    return render(request, 'treasure.html', {'treasure': search(request, Treasure)})


def hijab_link(request):

    return render(request, 'hijab.html', {'hijab': search(request, Hijab)})


def romol_link(request):
    return render(request, 'Romol.html', {'romol': search(request, Romol)})


def detail(request, pk):
    product = Product.objects.get(pk=pk)
    content = {"product": product}
    if request.POST:
        order(request, product=product )
        return render(request, "details.html", content)
    return render(request, "details.html", content)



def sh_detail(request, pk):
    shoe = Shoe.objects.get(pk=pk)
    content = {"shoe": shoe}
    if request.POST:
        order(request, product=shoe, )
        return render(request, "sh-detail.html", content)
    return render(request, "sh-detail.html", content)


def d_detail(request, pk):
    dresses = Dress.objects.get(pk=pk)
    content = {"dresses": dresses}
    if request.POST:
        order(request, product=dresses )
        return render(request, "d-detail.html", content)
    return render(request, "d-detail.html", content)


def b_detail(request, pk):
    bags = Bag.objects.get(pk=pk)
    content = {"bags": bags}
    if request.POST:
        order(request, product=bags)
        return render(request, "b-detail.html", content)

    return render(request, "b-detail.html", content)


def t_detail(request, pk):
    treasure = Treasure.objects.get(pk=pk)
    content = {"treasure": treasure}
    if request.POST:
        order(request, product=treasure)
        return render(request, "t-detail.html", content)

    return render(request, "t-detail.html", content)


def h_detail(request, pk):
    hijab = Hijab.objects.get(pk=pk)
    content = {"hijab": hijab}
    if request.POST:
        order(request, product=hijab)
        return render(request, "h-detail.html", content)

    return render(request, "h-detail.html", content)


def romol_detail(request, pk):
    romol = Romol.objects.get(pk=pk)
    content = {"romol": romol}
    if request.POST:
        order(request, product=romol)
        return render(request, "detail-r.html", content)

    return render(request, "detail-r.html", content)


