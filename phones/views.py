
from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_ = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'max_price':
        phone = phone_.order_by('-price')
    if sort == 'min_price':
        phone = phone_.order_by('price')
    if sort == 'name':
        phone = phone_.order_by('name')
    context = {'phones': phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
