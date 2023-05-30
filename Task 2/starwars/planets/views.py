from django.shortcuts import render

# Create your views here.
import requests

# from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.template.loader import render_to_string

# @cache_page(15)
def data(request):
    url = 'https://swapi.dev/api/planets/1/'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        residents = []
        for resident_url in data['residents']:
            resident_response = requests.get(resident_url)
            if resident_response.status_code == 200:
                resident_data = resident_response.json()
                residents.append(resident_data['name'])

        films = []
        for film_url in data['films']:
            film_response = requests.get(film_url)
            if film_response.status_code == 200:
                film_data = film_response.json()
                films.append(film_data['title'])

        del data['residents']
        del data['films']
        html = render_to_string('table.html', {'data': data, 'residents': residents, 'films': films})  
        response = HttpResponse(html, content_type='text/html')
        response['Cache-Control'] = 'public, max-age=20'  
        return response
        # return render(request, 'table.html', {'data': data, 'residents': residents, 'films': films})
    else:
        return render(request, 'table.html', {'data': None,'residents': None})


def req(request):
    return render(request, 'req.html')

def cached(request):
    return render(request, 'cached.html')

def table(request):
    return render(request, 'table.html')