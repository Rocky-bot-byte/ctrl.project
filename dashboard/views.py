from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from accounts.models import Notification, Profile
from requests.models import Booking
from providers.models import Provider
from services.models import Service

@login_required
def client_dashboard(request):
    user = request.user
    
    # Get or create profile
    profile, created = Profile.objects.get_or_create(user=user)
    
    # Get user's bookings
    bookings = Booking.objects.filter(user=user).order_by('-created_at')
    
    # Get unread notifications
    unread_notifications = Notification.objects.filter(user=user, is_read=False)
    
    # Recent notifications
    recent_notifications = Notification.objects.filter(user=user)[:5]
    
    # Get available services and providers for browsing
    available_services = Service.objects.select_related('provider').filter(available=True)[:6]
    available_providers = Provider.objects.all()[:6]
    
    context = {
        'profile': profile,
        'bookings': bookings,
        'unread_count': unread_notifications.count(),
        'recent_notifications': recent_notifications,
        'total_bookings': bookings.count(),
        'pending_bookings': bookings.filter(status='pending').count(),
        'completed_bookings': bookings.filter(status='completed').count(),
        'available_services': available_services,
        'available_providers': available_providers,
    }
    
    return render(request, 'dashboard/client_dashboard.html', context)

@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('client_dashboard')

@login_required
def client_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile.bio = request.POST.get('bio', '')
        profile.location = request.POST.get('location', '')
        profile.phone = request.POST.get('phone', '')
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('client_profile')
    
    return render(request, 'dashboard/client_profile.html', {'profile': profile})

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('home')
    
    # Admin statistics
    total_users = Profile.objects.count()
    total_providers = Provider.objects.count()
    total_services = Service.objects.count()
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='pending').count()
    
    # Recent bookings
    recent_bookings = Booking.objects.select_related('user', 'service', 'provider').order_by('-created_at')[:10]
    
    # Recent notifications sent
    recent_notifications = Notification.objects.filter(notification_type='admin_message').order_by('-created_at')[:5]
    
    context = {
        'total_users': total_users,
        'total_providers': total_providers,
        'total_services': total_services,
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'recent_bookings': recent_bookings,
        'recent_notifications': recent_notifications,
    }
    
    return render(request, 'dashboard/admin_dashboard.html', context)