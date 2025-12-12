from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service
from .forms import ServiceForm

def service_list(request):
    services = Service.objects.select_related('provider').all()
    return render(request, 'services/service_list.html', {'services': services})

@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully!')
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/add_service.html', {'form': form})