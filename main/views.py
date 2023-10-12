import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'app_name': "Warehouse Inventory",
        'name': request.user.username,
        'class': "PBP C",
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {"form": form}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        last_entry = Item.objects.latest('id')
        messages.info(request, f"Kamu telah menyimpan {last_entry.name} sebanyak {last_entry.amount} di Warehouse Inventory!")
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def delete(request, id):
    Item.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse("main:show_main"))

def decrement(request, id):
    item = Item.objects.get(pk=id)
    if item.amount == 1:
        messages.info(request, "Jumlah item tidak boleh kurang dari 1!")
    else:
        item.amount -= 1
        item.save(update_fields=["amount"])
    return HttpResponseRedirect(reverse("main:show_main"))

def increment(request, id):
    item = Item.objects.get(pk=id)
    item.amount += 1
    item.save(update_fields=["amount"])
    return HttpResponseRedirect(reverse("main:show_main"))

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def get_json_by_user(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data))