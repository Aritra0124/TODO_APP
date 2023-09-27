from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from todo_project.todo_app.forms import LoginForm, RegistrationForm
from django.contrib import messages


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print('here')
                login(request, user)

                return redirect('/')
            else:
                messages.error(request, 'username or password not correct')
                return redirect('/')
    else:
        login_form = LoginForm()
        registration_form = RegistrationForm()
        return render(request, 'index.html', {'login_form': login_form, 'registration_form': registration_form})
