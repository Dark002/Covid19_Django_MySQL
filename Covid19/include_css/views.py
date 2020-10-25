from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "include_css/index.html")