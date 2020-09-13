from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request,'simbaApp/home.html')
def clickhere_view(request):
    return render(request,'simbaApp/click.html')
