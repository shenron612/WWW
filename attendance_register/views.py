from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def event_list(request):
    return render(request, 'event_list.html')

def event_details(request):
    return render(request, 'event_details.html')

def about(request):
    return render(request, 'about.html')