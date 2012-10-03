# coding=utf-8
# файл с описанием Control'ов
from django.shortcuts import render_to_response
from Scoreboard.models import Flag

def check_flag(request):
    errors = []
    accepted = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append(u'Введите флаг.')
        else:
            try:
                Flag.objects.get(flag=q)
                accepted = True #добавить в базу флаг к команде
            except Flag.DoesNotExist:
                errors.append(u'Неверный флаг.')
    return render_to_response('check_form.html', {'accepted': accepted, 'errors': errors})