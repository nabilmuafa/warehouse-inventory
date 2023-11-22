import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json


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
            messages.success(
                request, 'Your account has been successfully created!')
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
            messages.info(
                request, 'Sorry, incorrect username or password. Please try again.')
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
        messages.info(
            request, f"Kamu telah menyimpan {last_entry.name} sebanyak {last_entry.amount} di Warehouse Inventory!")
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_product = Item.objects.create(
            user=request.user,
            name=data["name"],
            amount=int(data["amount"]),
            description=data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


@csrf_exempt
def add_items_ajax(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount,
                        description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()


@csrf_exempt
def delete(request):
    if request.method == "POST":
        item_id = request.POST.get("id")
        Item.objects.filter(pk=item_id).delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()


@csrf_exempt
def decrement(request):
    if request.method == "POST":
        item_id = request.POST.get("id")
        item = Item.objects.get(pk=item_id)
        if item.amount == 1:
            messages.info(request, "Jumlah item tidak boleh kurang dari 1!")
        else:
            item.amount -= 1
            item.save(update_fields=["amount"])
        return HttpResponse(status=201)
    return HttpResponseNotFound()


@csrf_exempt
def increment(request):
    if request.method == "POST":
        item_id = request.POST.get("id")
        item = Item.objects.get(pk=item_id)
        item.amount += 1
        item.save(update_fields=["amount"])
        return HttpResponse(status=201)
    return HttpResponseNotFound()


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
