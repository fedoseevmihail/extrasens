from django.shortcuts import render
from .models import Extrasens, NumUser, Extrasens_1, Extrasens_2


def index(request):
    template = 'extratest/index.html'
    title = 'Главная страница'
    context = {
            'title': title,
    }
    return render(request, template, context)

def examples(request):
    template = 'extratest/examples.html'
    title = 'Варианты экстрасенсов'
    num_extrasens_1 = Extrasens_1()
    num_extrasens_1.number = Extrasens_1.randint()
    num_extrasens_1.save()
    num_extrasens_2 = Extrasens_2()
    num_extrasens_2.number = Extrasens_2.randint()
    num_extrasens_2.save()
    context = {
        'num_extrasens_1': num_extrasens_1,
        'num_extrasens_2': num_extrasens_2,
        'title': title,
    }
    return render(request, template, context) 

def input_number(request):
    template = 'extratest/input_number.html'
    title = 'Страница ввода числа'
    if request.method == 'POST':
        num_user = NumUser()
        num_user.number = request.POST.get("num_user")
        num_user.save()
        context = {
            'num_user': num_user,
            'title': title,
        }
        return render(request, template, context)
        
    else:
        num_user = NumUser()
        context = {
            'num_user': num_user,
            'title': title,
        }
        return render(request, template, context)

def results(request):
    template = 'extratest/results.html'
    title = 'Результаты тестирования'
    list_num_extrasens_1 = Extrasens_1.objects.all()
    list_num_extrasens_2 = Extrasens_2.objects.all()
    list_num_user = NumUser.objects.all()
    rel_extrasens_2 = 0
    for num_extrasens_2 in list_num_extrasens_2:
        for num_user in list_num_user:
            if num_extrasens_2.number == num_user.number:
                rel_extrasens_2 += 1
            else:
                rel_extrasens_2 += 0
    #for num_extrasens_1 in list_num_extrasens_1:
    #    if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, num_extrasens_1, list_num_user), True):
    #        rel_extrasens_1 += 1
    #    else:
    #        rel_extrasens_1 += 0
    
    #for num_extrasens_1 in list_num_extrasens_1:
    #    if num_extrasens_1 in list_num_user:
    #        rel_extrasens_1 += 1
    #    else:
    #        rel_extrasens_1 += 0
    
    #for num_extrasens_1 in list_num_extrasens_1:
    #    for num_user in list_num_user:
    #        if num_extrasens_1.number == num_user.number:
    #            rel_extrasens_1 += 1
    #        else:
    #            rel_extrasens_1 -= 0
    #for i in range(len(list_num_extrasens_1)):
    #    if list_num_extrasens_1[i] == list_num_user[i]:
    #        rel_extrasens_1 += 1
    #    else:
    #        rel_extrasens_1 += 0
   
    context = {
        'list_num_extrasens_1': list_num_extrasens_1,
        'list_num_extrasens_2': list_num_extrasens_2,
        'list_num_user': list_num_user,
        'rel_extrasens_2': rel_extrasens_2,
        'title': title,
    }
    return render(request, template, context)

#rel_extrasens_1 = 0
    #filter_num = []
    #for num_extrasens_1 in list_num_extrasens_1:
    #    if num_extrasens_1.number == num_extrasens_1.reliability.number:
    #        rel_extrasens_1 += 1
    #    else:
    #        rel_extrasens_1 -= 0