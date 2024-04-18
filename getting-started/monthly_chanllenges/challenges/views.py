from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

from .data import challenges

def monthly_challenge(request: HttpRequest, month: str):
    try:
        challenge_text = challenges[month]
    except:
        return HttpResponseNotFound('Month not supported')
    return HttpResponse("%s: %s" % (month.capitalize(), challenge_text))


def monthly_challenge_by_number_month(request: HttpRequest, month: int):
    if month > 0 and month <= 12:
        keys =list(challenges.keys())
        month_name = keys[month - 1]
        challenge_text = challenges.get(month_name)
    else:
        return HttpResponseNotFound('Month not supported')
    return HttpResponse("%s: %s" % (month_name.capitalize(), challenge_text))

