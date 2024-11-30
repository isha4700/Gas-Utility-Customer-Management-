from django.shortcuts import render, redirect
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ServiceRequestForm
# Check if the user is an admin
def admin_check(user):
    return user.is_superuser

def home(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'main/dashboard.html', {'requests': requests})


@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            # Save the form (with user context)
            service_request = form.save(commit=False)
            service_request.user = request.user  # Assign the logged-in user
            service_request.save()
            messages.success(request, 'Service request submitted!')
            return redirect('dashboard')
    else:
        form = ServiceRequestForm()

    return render(request, 'main/create_request.html', {'form': form})
# Admin dashboard to manage service requests
@login_required
@user_passes_test(admin_check)
def admin_dashboard(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'main/admin_dashboard.html', {'requests': requests})

# Update service request status
@login_required
@user_passes_test(admin_check)
def update_request_status(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk)
    if request.method == 'POST':
        service_request.status = request.POST['status']
        service_request.save()
        messages.success(request, 'Status updated successfully!')
        return redirect('admin_dashboard')
    return render(request, 'main/update_request_status.html', {'service_request': service_request})
