from django.shortcuts import render, redirect, HttpResponse
from .forms import FileForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        data=request.FILES['myfile'].readlines()        
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        return render(request, 'output.html', { 'data':data })
    return render(request, 'index.html')


    