from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'project1_app/home.html')

def about_page(request):
    return render(request, 'project1_app/about.html')