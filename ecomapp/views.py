from django.shortcuts import render

# Create your views here.
from product.models import Product, Images


def home(request):
    product_obj = Product.objects.all().order_by('-id')[:2]
    new_product = Product.objects.all().order_by('-id')
    images = Images.objects.all().order_by('-id')[:2]
    products = Product.objects.all()
    context = {
        'products': product_obj,
        'product': products,
        'new_products': new_product,
        'images': images,
    }
    return render(request,'fontend/pages/home.html',context)


def single_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product_filter = Product.objects.filter(category=product.category)
    product_image = Images.objects.filter(product_id=product_id)
    context = {
        'product': product,
        'product_image': product_image,
        'filter_of_product': product_filter
    }
    return render(request,'fontend/pages/single_product.html',context)


