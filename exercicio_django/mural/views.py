from django.shortcuts import render, redirect
from .forms import RecadoForm
from .models import Recado

# Create your views here.
def boas_vindas(request):
    if request.method == "POST":
        form = RecadoForm(request.POST)
        if form.is_valid():
            recado = form.save(commit=False)
            recado.nome = recado.nome.title()
            recado.save()
            return redirect("boas_vindas")
    else:
        form = RecadoForm()
    recados = Recado.objects.order_by("-criado_em")
    contexto = {"form": form, "recados": recados}
    return render(request, "mural/boas_vindas.html", contexto)