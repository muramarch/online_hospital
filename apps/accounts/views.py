from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.accounts.forms import MyUserCreationForm, UserForm
from apps.accounts.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# user
def loginPage(request):
    page = 'login'

    # Hii ni kama mtu ka-login, apaswi kona login page unless ka-logout
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist.')

    context = {'page': page}
    return render(request, 'accounts/login_register.html', context)

# user
def logoutUser(request):
    logout(request)
    return redirect('home')


# user
def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong! Try again later.')

    return render(request, 'accounts/login_register.html', {'form': form})


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    appointments = user.appointment_set.all()

    context = {
        'user': user,
        'appointments': appointments,
    }
    return render(request, 'accounts/user_profile.html', context)


# user
@login_required(login_url='/login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    context = {'form': form}

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'accounts/update_user.html', context)