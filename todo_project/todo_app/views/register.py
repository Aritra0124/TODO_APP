from django.contrib.auth import login
from django.shortcuts import redirect
from todo_project.todo_app.forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            messages.success(request, 'registered')
            return redirect('/')
    else:
        return redirect('/')
