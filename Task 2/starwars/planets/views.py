from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse

def data(request):
    url = 'https://swapi.dev/api/planets/1/'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'Failed to fetch data'}, status=500)


def req(request):
    return render(request, 'req.html')