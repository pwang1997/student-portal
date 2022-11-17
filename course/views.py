from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def course_detail(request):
    return render(request, 'course_detail.html')

def course_list(request):
    return render(request, 'course_list.html')

def Xiong(request):
    return render(request, 'Xiong.html')

def test(request):
    return render(request, 'test.html')




# course add function
from .forms import Form
from django.forms import formset_factory
from .models import Course

def formset_view(request):
    context ={}
  
    # creating a formset
    GeeksFormSet = formset_factory(Form)
    formset = GeeksFormSet()
      
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "home.html", context)

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    # form = Form(request.POST or None)
    # if Course.is_valid():
    #     Course.save()
    Course_ID = request.POST.get('Course_ID')
    Course_name = request.POST.get('Course_name')
    Course_code = request.POST.get('Course_code')
    Section = request.POST.get('Section')
    Units = request.POST.get('Units')
    Days_and_time = request.POST.get('Days_and_time')
    Room =  request.POST.get('Room')
    Instructor = request.POST.get('Instructor')
    Meeting_Dates = request.POST.get('Meeting_Dates')
    Status = request.POST.get('Status')
    Capacity = request.POST.get('Capacity')
    Course_description = request.POST.get('Course_description')
    course = Course.objects.create(Course_ID=Course_ID,Course_name=Course_name,Course_code=Course_code,Section=Section,Units=Units,Days_and_time=Days_and_time,Room=Room,Instructor=Instructor,Meeting_Dates=Meeting_Dates,Status=Status,Capacity=Capacity,Course_description=Course_description)

    course.save()
    # form = Form(request.POST)
    # form.save()
    # context['form']= form
    return render(request, "create_view.html", context)

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] =Course.objects.all()
         
    return render(request, "list_view.html", context)



from django.shortcuts import (get_object_or_404,
							render,
							HttpResponseRedirect)



# after updating it will redirect to detail_View
def detail_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["data"] = Course.objects.get(id = id)
		
	return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# fetch the object related to passed id
	obj = get_object_or_404(Course, id = id)

	# pass the object as instance in form
	form = Form(request.POST or None, instance = obj)

	# save the data from the form and
	# redirect to detail_view
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/"+id)

	# add form dictionary to context
	context["form"] = form

	return render(request, "update_view.html", context)
