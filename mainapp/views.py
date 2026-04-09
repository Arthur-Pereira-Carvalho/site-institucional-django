from django.shortcuts import render, redirect
from .forms import ContatoForm

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def contato(request):
    sucesso = False

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contato/?sucesso=true')
    else:
        form = ContatoForm()

    if request.GET.get('sucesso'):
        sucesso = True

    return render(request, 'contato.html', {
        'form': form,
        'sucesso': sucesso
    })