from django.shortcuts import render
from .models import Extrasens, NumUser, Extrasens_1, Extrasens_2

from random import randint


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
    
    #rel_extrasens_1 = Extrasens_1.objects.all()
    #rel_extrasens_2 = Extrasens_2.objects.all()
    
    result = 0
    for num_extrasens_1 in Extrasens_1.objects.values("number"):
        if number["answer"] == answer["question__ans"]:
                    result += 1
                else:
                    result -= 0.33
        context.update({
            'result': result,
        })
    return render(request, 'result.html', context)
    
    filter_num = Extrasens_1()
    for num_extrasens_1 in list_num_extrasens_1:
        if num_extrasens_1.number != '':
            try:
                for num_user in list_num_user:
                    get_num = NumUser.objects.filter(number = num_extrasens_1.number)
                    if num_extrasens_1.number == get_num:
                        filter_num.reliability = 1
                        filter_num.save()
            except Exception:
                print('Нет совпадений')
                #filter_num.append(num_extrasens_1)
    #            context = {
     #               'list_num_extrasens_1': list_num_extrasens_1,
    #                'list_num_extrasens_2': list_num_extrasens_2,
     #               'list_num_user': list_num_user,
    #                'title': title,
    #                'rel_extrasens_1': filter_num,
    #           }
    #            return filter_num
    context = {
        'list_num_extrasens_1': list_num_extrasens_1,
        'list_num_extrasens_2': list_num_extrasens_2,
        'list_num_user': list_num_user,
        'rel_extrasens_1': filter_num,
        'title': title,
    }
    return render(request, template, context)
                # filter_num.append(num_extrasens_1)
            #except Exception:
                #filter_num.append(num_extrasens_1)
   # return render(request, template, context)


   filter_num = []
    for num_extrasens_1 in list_num_extrasens_1:
        if num_extrasens_1 != '':
            try:
                get_num = NumUser.objects.filter(number = num_extrasens_1.number)
                num_extrasens_1.reliability = get_num.reliability
                filter_num.append(num_extrasens_1)
                
            except Exception:
                filter_num.append(num_extrasens_1)