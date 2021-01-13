from store.models import Tshirt
from store.models import Occasion, Brand, Color, NeckType, IdealFor, Sleeve
from django.shortcuts import render
from django.core.paginator import Paginator
from urllib.parse import urlencode


def home(request):
    query = request.GET
    tshirts = []
    tshirts = Tshirt.objects.all()

    brand = query.get('brand')
    neckType = query.get('necktype')
    color = query.get('color')
    idealFor = query.get('idealfor')
    sleeve = query.get('sleeve')
    page = query.get('page')

    if page is None or page == '':
        page = 1

    if brand != '' and brand is not None:
        tshirts = tshirts.filter(brand__slug=brand)
    if neckType != '' and neckType is not None:
        tshirts = tshirts.filter(neck_type__slug=neckType)
    if color != '' and color is not None:
        tshirts = tshirts.filter(color__slug=color)
    if idealFor != '' and idealFor is not None:
        tshirts = tshirts.filter(ideal_for__slug=idealFor)
    if sleeve != '' and sleeve is not None:
        tshirts = tshirts.filter(sleeve__slug=sleeve)

    occassions = Occasion.objects.all()
    brands = Brand.objects.all()
    sleeves = Sleeve.objects.all()
    idealFor = IdealFor.objects.all()
    neckTypes = NeckType.objects.all()
    colors = Color.objects.all()

    paginator = Paginator(tshirts, 2)  # no of product you want to display
    page_object = paginator.get_page(page)

    query = request.GET.copy()
    query['page'] = ''
    pageurl = urlencode(query)

    context = {
        'page_object': page_object,
        'occassions': occassions,
        'brands': brands,
        'colors': colors,
        'sleeves': sleeves,
        'neckTypes': neckTypes,
        'idealFor': idealFor,
        'pageurl': pageurl,

    }
    return render(request, 'store/home.html', context=context)
