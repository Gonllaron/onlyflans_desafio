from django.shortcuts import render, redirect
from web.models import Flan, Contact
from web.forms import ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
    flanes_publicos = Flan.objects.filter(is_private=False)

    context = {
        'flanes_publicos': flanes_publicos
    }
    return render (request, "index.html", context)

def about (request):
    return render (request, "about.html")

@login_required
def welcome (request):
    flanes_privados = Flan.objects.filter(is_private=True)

    context = {
        'flanes_privados': flanes_privados
    }
    return render (request, "welcome.html", context)

def contacto (request):
        if request.method == 'GET':
            form = ContactForm()
            context = {'form':form}
            return render (request, 'contacto.html', context)
        else:
            form = ContactForm (request.POST)
            if form.is_valid():
                Contact.objects.create(
                    **form.cleaned_data
                )
                return redirect ('exito')
            context = {'form': form}
            return render (request, 'contacto.html', context)

def exito (request):
    return render (request, "exito.html")