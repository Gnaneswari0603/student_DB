from django.shortcuts import render , redirect                          
from .models import student
# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST.get('sname')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        course=request.POST.get('course')   
        print(name,age,phone,course)
        student.objects.create(name=name,age=age,mobile=phone,course=course)   
        print("successfully added the data to the databse")
        return redirect("display")
    
    return render(request,'register.html')  

def display(request):
    data=student.objects.all().order_by("-id")
    return render(request,'display.html',{'data':data})

def single_data(request,id):
    data1=student.objects.get(id=id)
    return render(request, 'single.html',{'data':data1})        


def edit(request,pk):
    data2=student.objects.get(id=pk)
    if request.method=="POST":
        name=request.POST.get('sname')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        course=request.POST.get('course')
        print(name,age,phone,course)
        data2.name=name
        data2.age=age
        data2.course=course
        data2.save()
        print("updated successfully")
    return render(request,'update.html',{'data':data2})
    
def delete_data(request,id):
    data3=student.objects.get(id=id)
    data3.delete()
    return redirect('display')
