from django.shortcuts import render

def homepageview(request):
    return render(request, 'index.html')