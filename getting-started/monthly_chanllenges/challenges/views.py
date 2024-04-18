from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

from .data import challenges

def monthly_challenge(request: HttpRequest, month: str):
    challenge_text = ""
    if month == "january":
        challenge_text = challenges['january']
    elif month == "february":
        challenge_text = challenges['february']
    elif month == "march":
        challenge_text = challenges['march']
    elif month == "april":
        challenge_text = challenges['april']
    elif month == "may":
        challenge_text = challenges['may']
    elif month == "june":
        challenge_text = challenges['june']
    elif month == "july":
        challenge_text = challenges['july']
    elif month == "august":
        challenge_text = challenges['august']
    elif month == "september":
        challenge_text = challenges['september']
    elif month == "october":
        challenge_text = challenges['october']
    elif month == "november":
        challenge_text = challenges['november']
    elif month == "december":
        challenge_text = challenges['december']
    else:
        return HttpResponseNotFound('Month not supported')
    return HttpResponse(challenge_text)


def monthly_challenge_by_number_month(request: HttpRequest, month: int):
    challenge_text = ""
    if month == 1:
        challenge_text = challenges['january']
    elif month == 2:
        challenge_text = challenges['february']
    elif month == 3:
        challenge_text = challenges['march']
    elif month == 4:
        challenge_text = challenges['april']
    elif month == 5:
        challenge_text = challenges['may']
    elif month == 6:
        challenge_text = challenges['june']
    elif month == 7:
        challenge_text = challenges['july']
    elif month == 6:
        challenge_text = challenges['august']
    elif month == 9:
        challenge_text = challenges['september']
    elif month == 10:
        challenge_text = challenges['october']
    elif month == 11:
        challenge_text = challenges['november']
    elif month == 12:
        challenge_text = challenges['december']
    else:
        return HttpResponseNotFound('Month not supported')
    return HttpResponse(challenge_text)

