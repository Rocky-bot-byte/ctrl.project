from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Service
from .forms import ServiceForm
from requests.models import Booking
from accounts.models import Notification

def service_list(request):
    services = Service.objects.select_related('provider').all()
    return render(request, 'services/service_list.html', {'services': services})

@login_required
def add_service(request):
    # Only allow staff/admin users to add services
    if not request.user.is_staff:
        messages.error(request, 'Access denied. Only administrators can add services.')
        return redirect('service_list')
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully!')
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/add_service.html', {'form': form})

@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        notes = request.POST.get('notes', '')
        
        # Create booking
        booking = Booking.objects.create(
            user=request.user,
            service=service,
            provider=service.provider,
            booking_date=booking_date,
            notes=notes,
            total_amount=service.price,
            status='pending'
        )
        
        # Create notification for user
        Notification.objects.create(
            user=request.user,
            title='Booking Confirmed',
            message=f'Your booking for {service.name} has been submitted and is pending approval.',
            notification_type='booking_confirmed'
        )
        
        # Create notification for admin (if admin exists)
        from django.contrib.auth.models import User
        admin_users = User.objects.filter(is_staff=True)
        for admin in admin_users:
            Notification.objects.create(
                user=admin,
                title='New Booking Request',
                message=f'New booking request from {request.user.username} for {service.name}',
                notification_type='admin_message'
            )
        
        messages.success(request, 'Booking request submitted successfully!')
        return redirect('client_dashboard')
    
    return render(request, 'services/book_service.html', {'service': service})