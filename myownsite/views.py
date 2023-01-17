from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from . import forms
from . import models

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def comm_new(request):
    if request.method == "POST":
        form = forms.Comm(request.POST)
        post = form.save(commit = False)
        post.user = request.user
        if models.Comments.objects.filter(user = request.user, kabinet = post.kabinet).exists() == 0:
            post.save()
        return redirect('home')
    else:
        form = forms.Comm()
    return render(request, 'new_comm.html', {'form' : form})

def home(request):
    kab = models.Kabinet.objects.all()
    return render(request, 'home.html', {'kab': kab})

def kab_detail(request, pk):
    kab = models.Kabinet.objects.get(pk=pk)
    coments=models.Comments.objects.filter(kabinet=kab)
    return render(request, 'kabinet_detail.html', {'kab': kab, 'coments':coments})