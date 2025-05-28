from django.shortcuts import render, HttpResponse

# Home Page.
def home(request):
    return render(request, "index.html")
