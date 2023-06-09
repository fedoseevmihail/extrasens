from django.shortcuts import render
from .models import NumUser, Extrasens_1, Extrasens_2, UserSession
from django.http import HttpResponse
from django.contrib.auth.signals import user_logged_in


#def user_logged_in_handler(sender, request, user, **kwargs):
#    UserSession.objects.get_or_create(user = user, session_id = request.session.session_key)

#user_logged_in.connect(user_logged_in_handler)

#def delete_user_sessions(user):
#    user_sessions = UserSession.objects.filter(user = user)
#    for user_session in user_sessions:
#        user_session.session.delete()

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
    request.session['username'] = 'mike'
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
    rel_extrasens_1 = 0
    rel_extrasens_2 = 0
    for i in range(len(list_num_extrasens_1)):
        if list_num_extrasens_1[i].number == list_num_user[i].number:
            rel_extrasens_1 += 1
        else:
            rel_extrasens_1 -= 1

    for i in range(len(list_num_extrasens_2)):
        if list_num_extrasens_2[i].number == list_num_user[i].number:
            rel_extrasens_2 += 1
        else:
            rel_extrasens_2 -= 1
   
    context = {
        'list_num_extrasens_1': list_num_extrasens_1,
        'list_num_extrasens_2': list_num_extrasens_2,
        'list_num_user': list_num_user,
        'rel_extrasens_1': rel_extrasens_1,
        'rel_extrasens_2': rel_extrasens_2,
        'title': title,
    }
    return render(request, template, context)
