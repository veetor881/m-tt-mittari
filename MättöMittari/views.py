from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ruoka, Arvio
from .forms import ArvioForm
from django.http import Http404

def index(request):
    return render(request, 'MättöMittari/index.html')

def ruoat(request):
    ruoat = Ruoka.objects.order_by('date_added')
    context = {'ruoat': ruoat}
    return render(request, 'MättöMittari/ruoat.html', context)

def ruoka(request, ruoka_id):
    ruoka = Ruoka.objects.get(id=ruoka_id)
    arviot = ruoka.arvio_set.order_by('-date_added')
    context = {'ruoka': ruoka, 'arviot': arviot}
    return render(request, 'MättöMittari/ruoka.html', context)

@login_required
def arvio(request, ruoka_id):
    ruoka = Ruoka.objects.get(id=ruoka_id)
    if request.method != 'POST':
        form = ArvioForm()
    else:
        form = ArvioForm(data=request.POST)
        if form.is_valid():
            arvio = form.save(commit=False)
            arvio.ruoka = ruoka
            arvio.owner = request.user
            arvio.save()
            return redirect('MättöMittari:ruoka', ruoka_id=ruoka_id)
    context = {'ruoka': ruoka, 'form': form}
    return render(request, 'MättöMittari/arvio.html', context)

@login_required
def muuta_arvio(request, arvio_id):
    arvio = Arvio.objects.get(id=arvio_id)
    if arvio.owner != request.user:
        raise Http404
    ruoka = arvio.ruoka

    if request.method != 'POST':
        form = ArvioForm(instance=arvio)
    else:
        form = ArvioForm(instance=arvio, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('MättöMittari:ruoka', ruoka_id=ruoka.id)
    context = {'arvio': arvio, 'ruoka': ruoka, 'form': form}
    return render(request, 'MättöMittari/muuta_arvio.html', context)

@login_required
def poista_arvio(request, arvio_id):
    arvio = Arvio.objects.get(id=arvio_id)
    if arvio.owner != request.user:
        raise Http404
    else:
        arvio.delete()
        return redirect('MättöMittari:ruoat')