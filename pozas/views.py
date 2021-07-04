from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from pozas.models import Poza, PozaCreateForm, PozaUpdateForm

# Create your views here.
def createPoza(request):
    form = PozaCreateForm()
    if request.method == 'POST':
        form = PozaCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'pozas/manage_pozas.html', context)

def updatePoza(request, pk):
    poza = Poza.objects.get(id=pk)
    form = PozaUpdateForm(instance=poza)
    if request.method == 'POST':
        form = PozaUpdateForm(request.POST, instance=poza)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'pozas/update_poza.html', context)