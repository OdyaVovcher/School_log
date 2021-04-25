from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddStudentForm

from .models import Student
# Create your views here.

def index(request):
	return render(request,"log/index.html")

def studentslist(request):
	students = Student.objects.all()
	return render(request, "log/studentslist.html",{"students":students})

def addstudent(request):

	if request.method == "POST":
		student = Student()
		student.name = request.POST.get("name")
		student.email = request.POST.get("email")
		student.birth_date = request.POST.get("birth_date")
		student.save()

		data = {"name":student.name, "email": student.email, "year": student.birth_date}

		return render(request, "log/student_info.html", context = data)
	else:
		addform = AddStudentForm()
		return render(request,"log/addstudent.html", {"form":addform})
