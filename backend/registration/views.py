from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


def view_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("../..")

    return render(request, 'login.html')
