from django.shortcuts import render

def splash(request):
    name = 'Billy'
    return render(request, "splash.html", {'name': name})