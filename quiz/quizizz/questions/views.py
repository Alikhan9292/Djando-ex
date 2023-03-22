from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError


def index(request):
    return HttpResponse("Страница приложения questions.")

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