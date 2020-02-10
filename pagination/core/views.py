from django.shortcuts import render
from .models import full_data
from django.db.models import Count

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    all_data=full_data.objects.values().annotate(Count('id_file'))
    print(str(all_data))
    return render(
        request,
        'index.html',
        context={'all_data':all_data},
    )