from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index2.html')
    
    #return HttpResponse("this is homepage")
def home(request):
    return render(request, 'index2.html')
    

def about(request):
    return render(request, 'aboutme.html')
    #return HttpResponse("this is about page")

def projects(request):
        return render(request, 'projects.html')

    #return HttpResponse("this is projects page")

def portfolio(request):
    return render(request, 'portfolio.html')

    #return HttpResponse("this is portfolio page")

def hireme(request):
    return render(request, 'hire me!.html')

    #return HttpResponse("this is portfolio page")

def Blog(request):
    return render(request, 'blog.html')

    #return HttpResponse("this is blog page")



