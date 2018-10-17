from django.contrib.auth.models import User

def signup_view(request):
    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['firstName']
    last_name = request.POST['lastName']
    user = User.objects.create_user(email, email, password)
    user.first_name = first_name
    user.last_name = last_name
    try:
        user.save()
    except Exception as e:
        print()
        # TODO
    return request