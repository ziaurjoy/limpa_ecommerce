from django.shortcuts import render, redirect,HttpResponseRedirect

# Create your views here.
from ecomapp.forms import MessageContactForm, SearchForms
from product.models import Product, Images, Category


def home(request):
    categorys = Category.objects.all()
    product_obj = Product.objects.all().order_by('-id')[:2]
    new_product = Product.objects.all().order_by('-id')
    images = Images.objects.all().order_by('-id')[:2]
    products = Product.objects.all()
    context = {
        'categorys': categorys,
        'products': product_obj,
        'product': products,
        'new_products': new_product,
        'images': images,
    }
    return render(request, 'fontend/pages/home.html', context)


def single_product(request,product_id):
    categorys = Category.objects.all()
    product = Product.objects.get(id=product_id)
    product_filter = Product.objects.filter(category=product.category)
    product_image = Images.objects.filter(product_id=product_id)
    context = {
        'categorys': categorys,
        'product': product,
        'product_image': product_image,
        'filter_of_product': product_filter
    }
    return render(request, 'fontend/pages/single_product.html', context)


def filter_of_categories(request,category_name):
    product_obj = Product.objects.all().order_by('-id')[:2]
    categorys = Category.objects.all()
    category_name = Category.objects.get(title=category_name)
    filtering_products = Product.objects.filter(category=category_name).order_by('-id')
    context = {
        'products': product_obj,
        'filtering_products': filtering_products,
        'categorys': categorys,
        'category_name': category_name
    }
    return render(request, 'fontend/pages/filter_of_categories.html', context)

def contact(request):
    forms = MessageContactForm()
    if request.method == "POST":
        forms = MessageContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('contact')

    categorys = Category.objects.all()
    context = {
        'forms': forms,
        'categorys': categorys,
    }
    return render(request, 'fontend/pages/contact.html', context)


def search_view(request):
    forms = SearchForms()
    if request.method == 'POST':
        forms = SearchForms(request.POST)
        if forms.is_valid():
            query = forms.cleaned_data['query']
            cat_id = forms.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query, category_id=cat_id)
            product_obj = Product.objects.all().order_by('-id')[:2]
            categorys = Category.objects.all()
            images = Images.objects.all().order_by('-id')[:2]
            context = {
                'products': product_obj,
                'filtering_products': products,
                'categorys': categorys,
                'query': query,
                'images': images,
            }
            return render(request, 'fontend/pages/filter_of_categories.html', context)
    product_obj = Product.objects.all().order_by('-id')[:2]
    categorys = Category.objects.all()
    images = Images.objects.all().order_by('-id')[:2]
    context = {
        'products': product_obj,
        'categorys': categorys,
        'images': images,
        'forms': forms
    }
    return render(request, 'fontend/pages/filter_of_categories.html', context)




