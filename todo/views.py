from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as userLogin, logout as userLogout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm


def account(request):
    context = {}

    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            first_name = request.POST.get('fullname')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if User.objects.filter(username=username).exists():
                error_message = "Username already exists"
                messages.error(request, error_message)

            elif password1 != password2:
                error_message = "Passwords do not match"
                messages.error(request, error_message)

            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name
                )
                user.save()
                messages.success(request, "Account created successfully")
                return redirect('account')

        except:
            error_message = "Invalid username or invalid credentials"
            messages.error(request, error_message)

    elif request.POST and 'login' in request.POST:
        context['login'] = True
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            userLogin(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password"
            messages.error(request, error_message)

    return render(request, 'account.html', context)

def logout(request):
    if request.user.is_authenticated:
        user = request.user
        userLogout(request)
        messages.success(request, "Logged out successfully")
    return redirect('account')

@login_required(login_url='account')
def home(request):
    user = request.user
    tasks = Todo.objects.filter(user=user)
    return render(request, 'home.html', {'tasks': tasks})

@login_required(login_url='account')
def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            print(f"Saved new task: {new_task.task}, User: {new_task.user}")
            
            return redirect('home')  
    else:
        form = TodoForm()
    
    return render(request, 'add_task.html', {'form': form})  # Replace 'home' with your actual URL name


@login_required(login_url='account')
def delete_task(request, pk):
    task = get_object_or_404(Todo, pk=pk, user=request.user)
    task.delete()
    return redirect('home')
    

@login_required(login_url='account')
def edit_task(request, pk):
    task = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})


@login_required(login_url='account')
def change_status(request, pk):
    task = get_object_or_404(Todo, pk=pk, user=request.user)
    if task:
        task.completed = not task.completed
        task.save()
    return redirect('home')


