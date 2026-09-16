from django.http import HttpResponse

# Create your views he

def index(reqeust):
    return HttpResponse("<h1>Hello World!</h1>")