from django.shortcuts import render
#from .models import Stud2

# Create your views here.
def form(request):
    return render(request,'form.html')
'''    obj=Stud2()
    name=request.POST.get("name")
    email=request.POST.get("email")
    age=request.POST.get("age")
    sex=request.POST.get("sex")
    contact=request.POST.get("contact")
    score=request.POST.get("score")
    course=request.POST.get("course")
    obj.name=name
    obj.email=email
    obj.age=age
    obj.sex=sex
    obj.contact=contact
    obj.score=score
    obj.course=course
    obj.save()'''
    
def insert(request):
    return render(request,'insert.html')