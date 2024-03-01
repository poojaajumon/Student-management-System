from django.shortcuts import render,redirect
from . models import Student
# Create your views here.
def index(request):
    data={
        "stu":Student.objects.all()
    }
    print(data)
    return render(request,'index.html',data)
def add(request):
    return render(request,'about.html')
def insert(request):
    if request.method=="POST":
        name=request.POST.get('name')
        print(name)
        school=request.POST.get('school')
        place=request.POST.get('place')
        query=Student(name=name,school=school,place=place)
        query.save()
    return redirect("/")    

def delete(request,id):
    dlt=Student.objects.get(id=id)
    dlt.delete()
    return redirect("/") 
def edit(request,id):
    data={"data":Student.objects.get(id=id)}
    return render(request,'edit.html',data)
def update(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        school=request.POST.get('school')
        place=request.POST.get('place')
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.school=school
        edit.place=place
        edit.save()
        return redirect("/")