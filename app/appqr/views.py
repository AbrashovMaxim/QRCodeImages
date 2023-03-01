from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .models import *

import qrcode
import qrcode.image.svg
import io
import base64

def QrCreateView(request):
    if request.method == 'POST':
        form = QrCreateForm(request.POST, request.FILES)

        if form.is_valid():
            check_data = form.cleaned_data
            mod = QrImageGenerator.objects.create(image_image=check_data['image'], user_id=request.user.id)

            messages.success(request, 'QR Создан!')
            return redirect('imageshow', id=mod.pk)

        else:
            messages.error(request, 'Ошибка в форме')
    else:
        form = QrCreateForm()
    
    return render(request, 'index.html', {'form': form})

def ImageShow(request, id):
    if request.method == 'GET':
        getImg = QrImageGenerator.objects.get(pk=id)
        nes = 'http://'+settings.ALLOWED_HOSTS[0]+redirect('imageshow', id=id).url
        img = qrcode.make(nes, image_factory=qrcode.image.svg.SvgImage)

        image = io.BytesIO()
        img.save(stream=image)
        base64_image = base64.b64encode(image.getvalue()).decode()

        return render(request, 'imageshow.html', {'image': getImg, 'svgqrcode': 'data:image/svg+xml;utf8;base64,' + base64_image})
    return redirect('imagecreate')

def ImageList(request):
    if request.method == 'GET':
        getImg = QrImageGenerator.objects.all().filter(user_id=request.user.id)
        for i in range(len(getImg)):
            nes = 'http://'+settings.ALLOWED_HOSTS[0]+redirect('imageshow', id=getImg[i].pk).url
            img = qrcode.make(nes, image_factory=qrcode.image.svg.SvgImage)

            image = io.BytesIO()
            img.save(stream=image)
            base64_image = base64.b64encode(image.getvalue()).decode()
            getImg[i].qr = 'data:image/svg+xml;utf8;base64,' + base64_image
            getImg[i].url_edit = redirect('imageedit', id=getImg[i].pk).url
        return render(request, 'imagelist.html', {'list': getImg})
    return redirect('imagecreate')

def ImageEdite(request, id):
    if request.method == 'GET':
        getImg = QrImageGenerator.objects.get(pk=id)

        return render(request, 'imageedit.html', {'image': getImg})
    else:
        if len(request.FILES['image_new']) > 0:
            s = QrImageGenerator.objects.get(pk=id)
            s.image_image = request.FILES['image_new']
            s.save()
            messages.success(request, 'Изображение успешно загружено')
            return redirect('imageedit', id=id)
        messages.error(request, 'Ошибка')
        return redirect('imageedit', id=id)


def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            check_Date = form.cleaned_data
            User.objects.create_user(username=check_Date['username'], password=check_Date['password'], first_name=check_Date['first_name'], last_name=check_Date['last_name'], email=check_Date['email'])
            messages.success(request, 'Вы успешно зарегистрировались')
            
            return redirect('login')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            check_Date = form.cleaned_data
            user = authenticate(request, username=check_Date['username'], password=check_Date['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно авторизовались')
                return redirect('imagelist')
            else:
                messages.error(request, 'Неправильный логин или пароль')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('imagecreate')