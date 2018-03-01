from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
#...

def redirect(request):
    return HttpResponseRedirect("analyze/")