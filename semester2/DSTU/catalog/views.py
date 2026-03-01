from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, "index.html")


def info(request, name):
    if name != 'Alex':
        return HttpResponseRedirect('/404')
    data = {'name': name}
    return render(request, 'info.html', context=data)


def not_found(request):
    return render(request, 'not_found.html')


def authors(request, name=None):
    if name is None:
        return render(request, 'authors.html')
    authors_list = [{'name': 'Alex', 'age': 30, 'released_courses': 10},
                    {'name': 'Tom', 'age': 40, 'released_courses': 20},
                    {'name': 'Bill', 'age': 50, 'released_courses': 30},
                    ]
    for author in authors_list:
        if name == author['name']:
            data = {"user": author}
            return render(request, 'author.html', context=data)
    return HttpResponseRedirect('/404')


def courses(request, id=None):
    if id is None:
        return render(request, 'authors.html')
    courses_list = [{'name': 'Математика', 'id': '00001', 'date': '3.12.2004'},
                    {'name': 'Физика', 'age': '00002', 'date': '7.12.2004'},
                    {'name': 'Русский', 'age': '00003', 'date': '10.12.2004'},
                    ]
    for course in courses_list:
        if id == course['name']:
            data = {"course": course}
            return render(request, 'author.html', context=data)
    return HttpResponseRedirect('/404')
