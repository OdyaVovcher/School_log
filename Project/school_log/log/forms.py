from django import forms

class AddStudentForm(forms.Form):
	name = forms.CharField()
	birthYear = forms.DateTimeField(input_formats=['%d/%m/%Y'])
	email = forms.EmailField()