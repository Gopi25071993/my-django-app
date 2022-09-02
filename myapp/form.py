from django import forms
from myapp.models import Student, Employees


class StuForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentForm(forms.Form):
    firstName = forms.CharField(label="Enter First Name", max_length=50)
    lastName = forms.CharField(label="Enter Last Name", max_length=100)
    email = forms.EmailField(label="Enter Email")
    file = forms.FileField() # for creating file input
    

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields= "__all__"