from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from orderapp.forms import ShopingCartForm
from orderapp.models import ShopCart
from product.models import Product,Category,Images


def add_to_shoping_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checking = ShopCart.objects.filter(product_id=id, user_id=current_user.id)
    if checking:
        control = 1
    else:
        control = 0
    if request.method == 'POST':
        forms = ShopingCartForm(request.POST)
        if forms.is_valid():
            if control == 1:
                data = ShopCart.objects.filter(
                    product_id=id, user_id=current_user.id)
                data.quantity += forms.cleaned_data['quantity']
                data.save()

            else:
                data = ShopCart()
                data.product_id = id
                data.user_id = current_user.id
                data.quantity = forms.cleaned_data['quantity']
                data.save()
        return HttpResponseRedirect(url)

    else:
        if control == 1:
            data = ShopCart.objects.filter(
                product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        return HttpResponseRedirect(url)

def card_details(request):
    categorys = Category.objects.all()
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for products in cart_product:
        total_amount += products.product.new_price * products.quantity
    context = {
        'categorys': categorys,
        'products': cart_product,
        'total_amount': total_amount,
    }
    return render(request, 'fontend/pages/shopping_cart.html', context)


def cart_delete(request, id):
    current_user = request.user
    url = request.META.get('HTTP_REFERER')
    card_obj = ShopCart.objects.filter(id=id, user_id=current_user.id)
    card_obj.delete()
    return HttpResponseRedirect(url)
