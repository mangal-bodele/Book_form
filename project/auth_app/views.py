from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def user_signup(request):
    template_name = 'auth_app/signup.html'
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    context = {'form': form}
    return render(request, template_name, context)

def user_login(request):
    template_name =  'auth_app/login.html'
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username =un , password=pw)
        if user:
            login(request, user)
        else:
            return HttpResponse('enter proper username or password')
    return render(request, template_name)

def user_logout(request):
    login(request)
    return redirect('login_url')

@login_required(login_url='login_url')
def pass_change(request):
    template_name = 'auth_app/change.html'
    if request.method == 'POST':
        old = request.POST['old']
        new = request.POST['new']
        user = request.user
        res = user.check_password(old)
        if res:
            user.set_password(new)
            user.save()
            return redirect('login_url')
    return render(request, template_name)

