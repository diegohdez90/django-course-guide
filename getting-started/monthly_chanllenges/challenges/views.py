from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

def monthly_challenge(request: HttpRequest, month: str):
    challenge_text = ""
    if month == "january":
        challenge_text = "Run"
    elif month == "february":
        challenge_text = "Read"
    elif month == "march":
        challenge_text = "Walk"
    elif month == "april":
        challenge_text = "Jump"
    elif month == "may":
        challenge_text = "Read"
    elif month == "june":
        challenge_text = "Run"
    elif month == "july":
        challenge_text = "Walk"
    elif month == "august":
        challenge_text = "Jump"
    elif month == "september":
        challenge_text = "Run"
    elif month == "october":
        challenge_text = "Walk"
    elif month == "november":
        challenge_text = "Jump"
    elif month == "december":
        challenge_text = "Read"
    else:
        return HttpResponseNotFound('Month not supported')
    return HttpResponse(challenge_text)

