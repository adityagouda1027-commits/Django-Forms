from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def djangoforms(request):

    ENFO=NameForm()

    d={'ENFO':ENFO}


    if request.method=='POST':
            NFDO=NameForm(request.POST)
            if NFDO.is_valid():
                  return HttpResponse(str(NFDO.cleaned_data))

            else:
                  return HttpResponse('Invalid data')
                
    return render(request, 'djangoforms.html',d)
