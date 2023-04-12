from django.shortcuts import render
from .models import Extrasens_1

from random import randint
from .forms import UserForm


def index(request):
    template = 'extratest/index.html'
    return render(request, template)

def examples(request):
    template = 'extratest/examples.html'
    extrasens1 = Extrasens_1.objects.all()
    num_random1 = randint(10, 99)
    num_random2 = randint(10, 99)
    title = 'Тестирование экстрасенсов'
    context = {
        'num_random1': num_random1,
        'num_random2': num_random2,
        'extrasens1': extrasens1,
        'title': title,
    }
    return render(request, template, context) 

def input_number(request):
    template = 'extratest/input_number.html'
    # num_user = request.POST.get("num_user")
    form = UserForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data.get("num_user")
        context = {
            'form': form,
            'data': data,
    }
        return render(request, template, context)
    return render(request, template) 