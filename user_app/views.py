from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


# Create your views here.
from product.models import Category
from user_app.forms import SignUpForm, UserUpdate, UpdateProfile
from user_app.models import UserProfile


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Username or Password')
    return render(request, 'fontend/pages/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def user_registration(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password, full_name=full_name)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'product/laptop1.jpg'

            data.save()
            return redirect('home')
        else:
            messages.warning(request, 'Your New password and re-password is not matching')
    context = {
        'form': form
    }
    return render(request, 'fontend/pages/register.html', context)


def user_profile(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    categorys = Category.objects.all()
    context = {
        'profile': profile,
        'categorys': categorys,
    }
    return render(request, 'fontend/pages/user_profile.html', context)

def update_profile(request):
    user_form = UserUpdate(instance=request.user)
    profile_form = UpdateProfile(instance=request.user.userprofile)
    if request.method == 'POST':
        user_form = UserUpdate(request.POST, instance=request.user)
        profile_form = UpdateProfile(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile has been updated')
            return redirect('user-profile')
    categorys = Category.objects.all()
    context = {
        'user_form': user_form,
        "profile_form": profile_form,
        'categorys': categorys,

    }
    return render(request, 'fontend/pages/update_profile.html', context)



def password_change(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your Password Changeing is done')
            return redirect('user-profile')
        else:
            messages.error(request, 'Please correct the error below.<b>'+str(form.errors))
            return redirect('change-password')
    categorys = Category.objects.all()
    context = {
        'form': form,
        'categorys': categorys

    }
    return render(request, 'fontend/pages/change_password.html', context)



