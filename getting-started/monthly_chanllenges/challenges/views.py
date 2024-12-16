from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

from .data import challenges

def index(request):
    months = list(challenges.keys())
    items = ""
    for month in months:
        month_path = reverse('monthly_challenge', args=[month])
    
    return render(request, 'index.html', context={
        'months': months
    })


def monthly_challenge(request: HttpRequest, month: str):
    try:
        challenge_text = challenges[month]
        html = render_to_string(template_name='challenge.html',
                                context={
                                    'text': challenge_text,
                                    'month': month.capitalize()
                                })
        # html = render(request, 'challenge.html',
        #               context={
        #                   'text': challenge_text,
        #                   'month': month.capitalize()
        # })
    except:
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)
    return HttpResponse(html)


def monthly_challenge_by_number_month(request: HttpRequest, month: int):
    try:
        keys =list(challenges.keys())
        month_name = keys[month - 1]
        redirect_path = reverse('monthly_challenge', args=[month_name])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()
    
