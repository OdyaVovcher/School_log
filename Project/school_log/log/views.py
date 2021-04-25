from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddStudentForm
# Create your views here.

def index(request):
	return render(request,"log/index.html")

def studentlist(request):
	return HttpResponse("Список студентов")

def addstudent(request):

	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		birthYear = request.POST.get("birthYear")
		subjects = request.POST.get("subjects")

		data = {"name":name, "email": email, "year": birthYear}
		return render(request, "log/student_info.html", context = data)
	else:
		addform = AddStudentForm()
		return render(request,"log/addstudent.html", {"form":addform})
