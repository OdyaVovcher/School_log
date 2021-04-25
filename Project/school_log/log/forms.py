from django import forms

class AddStudentForm(forms.Form):
	name = forms.CharField()
	birth_date= forms.DateTimeField(input_formats=['%Y-%m-%d'])
	email = forms.EmailField(max_length=30)