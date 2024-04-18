from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from .data import challenges

def monthly_challenge(request: HttpRequest, month: str):
    try:
        challenge_text = challenges[month]
    except:
        return HttpResponseNotFound('Month not supported')
    return HttpResponse("%s: %s" % (month.capitalize(), challenge_text))


def monthly_challenge_by_number_month(request: HttpRequest, month: int):
    try:
        keys =list(challenges.keys())
        month_name = keys[month - 1]
        return HttpResponseRedirect("/challenges/%s" % month_name)
    except:
        return HttpResponseNotFound('Month not supported. Try again')
    
