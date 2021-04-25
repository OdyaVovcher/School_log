from django import forms

class AddStudentForm(forms.Form):
	name = forms.CharField()
	birthYear = forms.DateTimeField(input_formats=['%d/%m/%Y'])
	email = forms.EmailField()

	SUBJECTS = (('1','CSS'),("2", "HTML"),("3","JS"))
	subjects = forms.MultipleChoiceField(choices=SUBJECTS, 
	widget=forms.CheckboxSelectMultiple())