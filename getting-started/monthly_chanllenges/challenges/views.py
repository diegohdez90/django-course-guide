from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from .data import challenges

def index(request):
    months = list(challenges.keys())
    items = ""
    for month in months:
        month_path = reverse('monthly_challenge', args=[month])
        month_capitalize = month.capitalize()
        items = items + f"""
                <li>
                    <a href=\"{month_path}\">{month_capitalize}</a>
                </li>
            """
    html = f"""
            <ul>
                {items}
            </ul>
        """
    return HttpResponse(html)


def monthly_challenge(request: HttpRequest, month: str):
    try:
        challenge_text = challenges[month]
        html = f"""
                <h1>{month.capitalize()}: {challenge_text}</h1>
            """
    except:
        return HttpResponseNotFound('<h1>Month not supported</h1>')
    return HttpResponse(html)


def monthly_challenge_by_number_month(request: HttpRequest, month: int):
    try:
        keys =list(challenges.keys())
        month_name = keys[month - 1]
        redirect_path = reverse('monthly_challenge', args=[month_name])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound('<h1>Month not supported. Try again</h1>')
    
