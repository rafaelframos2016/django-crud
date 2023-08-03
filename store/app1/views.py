from django.shortcuts import render
from .models import User
from .forms import UserFrom

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request,'index.html',context)

def criar(request):
    if request.method == 'GET':
        form = UserFrom()
        context = {
            'form':form
        }
        return render(request,'criar.html',context)
    else:
        form = UserFrom(request.POST)
        if form.is_valid():
            form.save()
            users = User.objects.all()
            context = {
                'users': users
            }      
            return render(request,'index.html',context)