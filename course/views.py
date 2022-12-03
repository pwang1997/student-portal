from django.shortcuts import (get_object_or_404,
							render, redirect,
							HttpResponseRedirect)
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from .models import Course

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
    
    form = Form(request.POST)
    context['form']= form
    return render(request, "create_view.html", context)

def handle_create_course(request):
    if request.method != "POST":
        return HttpResponseBadRequest(f'This view can not handle method {format(request.method)}', status=405)
        
    # add the dictionary during initialization
    name = request.POST.get('name')
    department = request.POST.get('department')
    code = request.POST.get('code')
    section = request.POST.get('section')
    units = request.POST.get('units')
    timetable = request.POST.get('timetable')
    location =  request.POST.get('location')
    instructor = request.POST.get('instructor')
    course_dates = request.POST.get('course_dates')
    status = request.POST.get('status')
    capacity = request.POST.get('capacity')
    description = request.POST.get('description')

    course = Course(name=name,code=code,
                    department=department,
                    section=section,units=units,
                    timetable=timetable,
                    location=location,instructor=instructor,
                    course_dates=course_dates,status=status,
                    capacity=capacity,description=description)

    course.save()

    return redirect('/course/list')

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] =Course.objects.all()
         
    return render(request, "list_view.html", context)

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
		return HttpResponseRedirect("/course/detail_view/"+str(id))

	# add form dictionary to context
	context["form"] = form

	return render(request, "update_view.html", context)


def search(request):
    if  request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Course.objects.filter(name__contains=query_name)
            return render(request, 'search.html', {"results":results})
        
    return render(request, 'search.html')