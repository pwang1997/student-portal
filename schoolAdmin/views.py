from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.contrib import messages
from user.models import Users

# Create your views here.
def index(request):
    return HttpResponse("Admin Dashboard")

def professor(request):
    return HttpResponse("Admin Dashboard: Page Professor List")

def course(request):
    return HttpResponse("Admin Dashboard: Page Course List")

def student(request):
    return HttpResponse("Admin Dashboard: Page Student List")

def login(request):
    template = loader.get_template('./login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def handle_admin_login(request):
    if request.method != "POST":
        return HttpResponseBadRequest(f'This view can not handle method {format(request.method)}', status=405)
    
    username = request.POST.get('uname')
    password = request.POST.get('psw')
    
    user = Users.objects.filter(username=username, 
                                password=password)
    print(user)
    return HttpResponse(status=200)