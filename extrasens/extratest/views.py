from django.shortcuts import render, redirect
from .models import Extrasens_1, NumUser

from random import randint
from .forms import UserForm


def index(request):
    template = 'extratest/index.html'
    return render(request, template)

def examples(request):
    template = 'extratest/examples.html'
    num_extrasens_1 = Extrasens_1.objects.all()
    list_num_user = NumUser.objects.all()
    num_random1 = randint(10, 99)
    num_random2 = randint(10, 99)
    title = 'Тестирование экстрасенсов'
    context = {
        'num_random1': num_random1,
        'num_random2': num_random2,
        'num_extrasens_1': num_extrasens_1,
        'title': title,
        'list_num_user': list_num_user,
    }
    return render(request, template, context) 

def input_number(request):
    template = 'extratest/input_number.html'
    if request.method == 'POST':
        num_user = NumUser()
        num_user.number = request.POST.get("number")
        num_user.save()
        context = {
            'num_user': num_user,
        }
        return render(request, template, context)
        
    else:
        num_user = NumUser()
        #num_user = request.GET.get('num_user')
        #list_num_user = UserForm.filter(num_user=num_user)
        #list_num_user.save()
        #context = {
        #    'num_user': num_user,
            #'list_num_user': list_num_user,
        #}
        return render(request, template, {'num_user': num_user,})
        
    #return render(request, template, context)
    #return render(request, template, {'form': form,})
