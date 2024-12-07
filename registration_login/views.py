from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from pet_registration.models import Pet
from django.views.decorators.csrf import ensure_csrf_cookie
from veterinarians.models import MedicalRecord, BillingRecord

#Authentication models and functions

#Import Profile and UserDetails

def homepage(request):
    return render(request, 'mainpages/homepage.html')

def landingpage(request):
    return render(request, 'mainpages/landingpage.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Save the User instance
            user = form.save()

            # Create or get the Profile for the new user
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'first_name': form.cleaned_data.get('first_name'),
                    'last_name': form.cleaned_data.get('last_name'),
                    'role': form.cleaned_data.get('role'),
                }
            )
            
            if not created:
                # Update existing profile with form data
                profile.first_name = form.cleaned_data.get('first_name')
                profile.last_name = form.cleaned_data.get('last_name')
                profile.role = form.cleaned_data.get('role')
                profile.save()

            messages.success(request, 'Registration successful! Please log in.')
            return redirect('registration_login:registration_success') 
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'registration_login/register.html', context=context)

def my_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back {username}!')
                
                # Check if user is a veterinarian
                if hasattr(user, 'profile') and user.profile.role == 'VET':
                    return redirect('veterinarians:dashboard')  # Redirect to vet dashboard
                
                # Get the next URL if it exists
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                    
                return redirect('homepage:index')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'registration_login/my_login.html', context=context)

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('homepage:index')

def registration_success(request):
    return render(request, 'registration_login/registration_success.html')

def set_appointment(request):
    # Add your appointment logic here
    return render(request, 'appointments/set_appointment.html')

#def all_user(request):
#    return HttpResponse('Returning all user')

@login_required
def profile(request):
    if request.user.profile.role == 'VET':
        return redirect('veterinarians:vet_profile')
    
    # Count pets
    pets_count = Pet.objects.filter(owner=request.user).count()
    
    # Count appointments
    appointments_count = sum(pet.appointments.count() for pet in request.user.pets.all())
    
    # Count pending bills using a more efficient query
    pending_bills_count = BillingRecord.objects.filter(
        medical_record__pet__owner=request.user,
        status='PENDING'
    ).count()
    
    context = {
        'pets_count': pets_count,
        'appointments_count': appointments_count,
        'pending_bills_count': pending_bills_count,
    }
    return render(request, 'registration_login/profile.html', context)

@login_required
@ensure_csrf_cookie
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        try:
            # Print debug information
            print("Form data:", request.POST)
            print("Files:", request.FILES)

            # Update profile fields with validation
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            
            if not first_name or not last_name or not email:
                messages.error(request, 'First name, last name, and email are required.')
                return render(request, 'registration_login/edit_profile.html', {'profile': profile})
            
            # Update basic information
            profile.first_name = first_name
            profile.last_name = last_name
            profile.address = request.POST.get('address', '')
            profile.contact_number = request.POST.get('contact_number', '')
            
            # Update payment information if user is an owner
            if profile.role == 'OWNER':
                preferred_payment = request.POST.get('preferred_payment')
                if preferred_payment in dict(profile.PAYMENT_CHOICES):
                    profile.preferred_payment = preferred_payment
                    
                    if preferred_payment == 'CARD':
                        profile.card_number = request.POST.get('card_number', '')
                        profile.card_expiry = request.POST.get('card_expiry', '')
                        profile.ewallet_number = ''  # Clear e-wallet if switching to card
                    elif preferred_payment in ['GCASH', 'MAYA']:
                        profile.ewallet_number = request.POST.get('ewallet_number', '')
                        profile.card_number = ''  # Clear card details if switching to e-wallet
                        profile.card_expiry = ''
            
            # Handle profile picture upload
            if 'profile_picture' in request.FILES:
                file = request.FILES['profile_picture']
                
                # Validate file type
                if not file.content_type.startswith('image/'):
                    messages.error(request, 'Invalid file type. Please upload an image file.')
                    return render(request, 'registration_login/edit_profile.html', {'profile': profile})
                
                # Delete old profile picture if it exists and is not the default
                if profile.profile_picture and 'profile.png' not in profile.profile_picture.name:
                    try:
                        profile.profile_picture.delete(save=False)
                    except Exception as e:
                        print(f"Error deleting old profile picture: {e}")
                
                profile.profile_picture = file
            
            # Update user email
            request.user.email = email
            request.user.save()
            
            # Save profile changes
            profile.save()
            
            messages.success(request, 'Profile updated successfully!')
            return render(request, 'registration_login/edit_profile.html', {'profile': profile})
            
        except Exception as e:
            print(f"Error updating profile: {e}")
            messages.error(request, 'An error occurred while updating your profile.')
            return render(request, 'registration_login/edit_profile.html', {'profile': profile})
    
    return render(request, 'registration_login/edit_profile.html', {'profile': profile})