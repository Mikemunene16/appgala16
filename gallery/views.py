from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def index(request):
    title = "Welcome to appgala, showcasing galleries"
    images = Image.objects.all()
    return render(request, 'main/index.html', locals())

def category(request):
    title = "Categories of appgala"
    images = Image.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/category.html', locals())

def search_image(request):
    if 'image' in request.GET and request.GET["image"]:
        searched_image = request.GET.get("image")
        images = Image.searching_image(searched_image)
        term = f"{searched_image}"
        return render(request, 'main/search.html', locals())
    else:
        message = "Kindly input an image name to get results"
        return render(request, 'main/search.html', locals())