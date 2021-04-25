from django import forms

class AddStudentForm(forms.Form):
	name = forms.CharField()
	age = forms.IntegerField()
	email = forms.EmailField(max_length=30)