from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            return HttpResponse('Usuário já cadastrado!')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse(f'New user created {username} de id {user.id}')
            
        return HttpResponse(f'Usuário: {username} - Email: {email} - Senha: {password}')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request,user)
            return HttpResponse('Autenticação bem sucessida!')
        else:
            return HttpResponse('Usuário ou senha inválidos!')
        
login_required(login_url='/login/')
def plataform(request):
    if request.user.is_authenticated:
        return HttpResponse('Você está autenticado')
    else:
        return HttpResponse('Vá imbora')
