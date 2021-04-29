from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddStudentForm

from .models import Student, Course
# Create your views here.

def index(request):
	return render(request,"log/index.html")

def courses(request):
	courses = Course.objects.all()
	return render(request,"log/courses.html", {"courses":courses})

def studentslist(request):
	students = Student.objects.all().order_by('name')
	return render(request, "log/studentslist.html",{"students":students})

def student_info(request,id):
	student = Student.objects.get(id = id)
	courses = student.courses.all()
	return render(request, "log/student_info.html",{"student":student,"courses":courses})

def addstudent(request):

	if request.method == "POST":
		student = Student()
		student.name = request.POST.get("name")
		student.age = request.POST.get("age")
		student.email = request.POST.get("email")
		student.save()
		subjects = request.POST.getlist("subjects")
		for subject in subjects:
			course, created = Course.objects.get_or_create(name = subject)
			if created:
				course.save()
			course.student_set.add(student)
			course.save()
		return HttpResponseRedirect("/")
	else:
		addform = AddStudentForm()
		return render(request,"log/addstudent.html", {"form":addform})


def edit(request, id):
	try:
		student = Student.objects.get(id = id)

		if request.method == "POST":
			student.name = request.POST.get("name")
			student.age = request.POST.get("age")
			student.save()
			return HttpResponseRedirect("/")
		else:
			return render(request, "log/edit.html", {"student": student})

	except Student.DoesNotExist:
		return HttpResponseNotFound("<h2>Student not found</h2>")


def delete(request,id):
	try:
		student = Student.objects.get(id = id)
		student.delete()
		return HttpResponseRedirect("/")
	except Student.DoesNotExist:
		return HttpResponseNotFound("<h2>Student not found</h2>")

def show_course_students(request, name):
	course = Course.objects.filter(name = name)
	students = Student.objects.filter(courses__name = name)
	return render(request, "log/course_students.html",{"course":course,"students":students, "name":name})