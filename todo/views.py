from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import Todo
from .forms import TodoForm
# Create your views here.

def login(request):
    return render(request,'login.html')



def home(request):
    tasks = Todo.objects.all()
    return render(request,'home.html',{'tasks':tasks})
    

def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        return render(request,'add_task.html')
    
def delete_task(request,pk):
    
    task = get_object_or_404(Todo, pk=pk)
    if task:
        task.delete()
        return redirect('/')
    else:
        return redirect('/')  
    
def edit_task(request,pk):
    task = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance=task)
        return render(request,'edit_task.html',{'form':form})  
    
def change_status(request,pk):
    task = get_object_or_404(Todo, pk=pk)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('/')
    else:
        return redirect('/')   
