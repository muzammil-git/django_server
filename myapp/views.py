from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Muzammil"
    hobby = "Soccer"
    map = {
        'name' : name, 
        'hobby' : hobby
    }

    return render(request, 'index.html', map)
    # return HttpResponse('<h1> Hey Welcome </h1>')

def counter(request):
    sentence = request.POST['sentence']
    print(sentence)
    return render(request, 'counter.html', {'sentence': sentence})


def about_us(request):
    return render(request, 'about_us.html')