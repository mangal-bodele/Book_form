from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import BookForm
from django.http import HttpResponse
from .models import Book
@login_required(login_url='login_url')
def add_book(request):
    template_name = 'crud_app/add.html'
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)
@login_required(login_url='login_url')
def show_book(request):
    template_name = 'crud_app/show.html'
    books = Book.objects.all()
    context = {'books':books}
    return render(request, template_name, context)

def update_book(request, pk):
    template_name = 'crud_app/add.html'
    obj = Book.objects.get(id=pk)
    form = BookForm(instance=obj)
    if request.method == "POST":
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form' : form}
    return render(request, template_name, context)

def delete_book(request, pk):
    template_name = 'crud_app/confirm.html'
    obj = Book.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, template_name)


