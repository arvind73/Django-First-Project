from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
# Create your views here.


def help(request):
    help_dict = {'help_insert':"HELP PAGE"}
    return render(request,'second_app/help.html',context=help_dict)

def home(request):
    return HttpResponse("<em>This is the home page!</em>")

def start(request):
    return render(request, 'second_app/start.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'second_app/users.html',context=user_dict)

