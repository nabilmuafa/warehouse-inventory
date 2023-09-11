from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': "Pacil Warehouse Inventory",
        'name': "Muhammad Nabil Mu'afa",
        'class': "PBP C"
    }

    return render(request, "main.html", context)
