from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def info(request):
    name = request.GET.get('name', 'Guest')
    password = request.GET.get('password', 'None')
    data = {'name': name, 'password': password}
    return render(request, 'info.html', context=data)
