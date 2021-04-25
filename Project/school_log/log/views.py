from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddStudentForm

from .models import Student
# Create your views here.

def index(request):
	return render(request,"log/index.html")

def studentslist(request):
	students = Student.objects.all()
	return render(request, "log/studentslist.html",{"students":students})

def student_info(request):
	return render(request, "log/shortcuts.html")

def addstudent(request):

	if request.method == "POST":
		student = Student()
		student.name = request.POST.get("name")
		student.age = request.POST.get("age")
		student.email = request.POST.get("email")

		student.save()

		data = {"name":student.name, "email": student.email, "age": student.age}

		return render(request, "log/student_info.html", context = data)
	else:
		addform = AddStudentForm()
		return render(request,"log/addstudent.html", {"form":addform})


def edit(request, id):
	try:
		student = Student.objects,get(id = id)

		if request.method == "POST":
			student.name = request.POST.get("name")
			student.email = request.POST.get("email")
			student.age = request.POST("age")
			student.save()
			return HttpResponseRedirect("/")
		else:
			return render(request, "edit.html", {"person": person})

	except Student.DoesNotExist:
		return HttpResponseNotFound("<h2>Student not found</h2>")


def delete(request,id):
	try:
		student = Student.objects.get(id = id)
		student.delete()
		return HttpResponseRedirect("/")
	except Student.DoesNotExist:
		return HttpResponseNotFound("<h2>Student not found</h2>")