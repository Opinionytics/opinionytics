from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def signin_view(request):
    username = request.POST['textfield']
    password = request.POST['passwordfield']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("ok")
        return redirect("../analyze")
    # TODO