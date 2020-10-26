from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from orderapp.forms import ShopingCartForm
from orderapp.models import ShopCart


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