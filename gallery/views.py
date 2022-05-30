from django.shortcuts import render

# Create your views here.
def index(request):
    title = "Welcome to appgala, showcasing galleries"
    return render(request, 'main/index.html', locals())

def hello(request):
    title = "Hello there, 2nd page works"
    return render(request, 'main/hello.html', locals())