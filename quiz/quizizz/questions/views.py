from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render
from .forms import ContactForm

from .models import *



def index(request):
    posts = Quiz.objects.all()
    return render(request, 'questions/index.html', {'posts': posts})
def quiz(request):
    return render(request, 'questions/index.html')

def about(request):
    return render(request, 'questions/about.html')

def contact(request):
    return render(request, 'questions/contact.html')

def quiz_detail(request):
    # реализация логики для отображения викторины
    return render(request, 'questions/quiz_detail.html')



def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # обработка формы
            pass
    return render(request, 'questions/contact.html', {'form': form})



def categories(request, catid):
    if (request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1>{catid}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def badRequest(request, exception):
    return HttpResponseBadRequest('Плохой запрос')

def permissionDenied(request, exception):
    return HttpResponseForbidden('В разрешении отказано')

def serverError(request):
    return HttpResponseServerError('Внутренняя ошибка сервера')
