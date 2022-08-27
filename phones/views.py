from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    all_phones = Phone.objects.all()
    if sort_pages == 'low':
        all_phones = all_phones.order_by('price')
    elif sort_pages == 'high':
        all_phones = all_phones.order_by('-price')
    elif sort_pages == 'alph':
        all_phones = all_phones.order_by('name')
    context = {'phones': all_phones,
               }
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug)
    context = {'phone': phone}
    return render(request, template, context=context)
