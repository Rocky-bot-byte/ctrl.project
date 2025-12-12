from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Provider
from .forms import ProviderForm

def provider_list(request):
    providers = Provider.objects.all()
    return render(request, 'providers/provider_list.html', {'providers': providers})

@login_required
def add_provider(request):
    # Only allow staff/admin users to add providers
    if not request.user.is_staff:
        messages.error(request, 'Access denied. Only administrators can add providers.')
        return redirect('provider_list')
    
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Provider added successfully!')
            return redirect('provider_list')
    else:
        form = ProviderForm()
    return render(request, 'providers/add_provider.html', {'form': form})