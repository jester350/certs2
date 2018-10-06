#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import cert
from django.utils import timezone
from .forms import CertForm
# Create your views here.
from django.shortcuts import redirect, HttpResponse

def cert_list(request):
    certs = cert.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'cert/cert_list.html', {'certs': certs})

def cert_detail(request, pk):
    certs = get_object_or_404(cert, pk=pk)
    return render(request, 'cert/cert_detail.html', {'certs': certs})
    #certs = cert.objects.get(pk=pk)
    #return render(request, 'cert/cert_detail.html', {'certs': certs})

def cert_new(request):
    form = CertForm()
    return render(request, 'cert/cert_edit.html', {'form': form})

def cert_new(request):
    form = CertForm()
    return render(request, 'cert/cert_edit.html', {'form': form})

def cert_new(request):
    if request.method == "POST":
        form = CertForm(request.POST)
        if form.is_valid():
            cert = form.save(commit=False)
            cert.auther = request.user
            cert.published_date = timezone.now()
            cert.save()
            return redirect('cert_detail', pk=cert.pk)
    else:
        form = CertForm()
    return render(request, 'cert/cert_edit.html', {'form': form})
