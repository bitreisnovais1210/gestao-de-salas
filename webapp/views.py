from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def bem_vindo(request):
    """View de boas-vindas"""
    return render(request, 'webapp/bem_vindo.html')


def login_view(request):
    """View de login"""
    if request.user.is_authenticated:
        return redirect('webapp:bem_vindo')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('webapp:bem_vindo')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'webapp/login.html')


def registro_view(request):
    """View de registro/cadastro"""
    if request.user.is_authenticated:
        return redirect('webapp:bem_vindo')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if not username or not password:
            messages.error(request, 'Usuário e senha são obrigatórios.')
        elif password != password_confirm:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('webapp:login')
    
    return render(request, 'webapp/registro.html')


@login_required
def logout_view(request):
    """View de logout"""
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('webapp:login')
