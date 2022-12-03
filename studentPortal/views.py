from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from student.models import Student
from professor.models import Professor

def login(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_type = request.POST.get("user-role")
        
        is_user_exists = []
        
        if user_type == "student":
            is_user_exists = Student.objects.filter(email=email, password=password)
        elif user_type == "professor":
            is_user_exists = Professor.objects.filter(email=email, password=password)
            
        if is_user_exists.__len__() == 0:
            return HttpResponseBadRequest("Invalid User Credentials", status=400)

        request.session['user'] = {"id": is_user_exists[0].pk, "role": user_type}
        return redirect('/student/') if user_type == "student" else redirect("/professor/")

    return render(request, 'login.html')