import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .google_bard import get_response

def index(request):
    return render(request, "index.html")

def google_bard_response(request):
    response = get_response(request.GET.get('prompt'))
    return JsonResponse({'message': response})
    # return HttpResponse(json.dumps(response),)
