from django.shortcuts import render

def bem_vindo(request):
    """View de boas-vindas"""
    return render(request, 'webapp/bem_vindo.html')
