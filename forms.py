from django import forms
# from .models import Employeedb

from .models import Contact

# class EmployeeForm(forms.Form):
#     name=forms.CharField(max_length=100)
#     email=forms.EmailField()
#     age=forms.IntegerField()
#     salary=forms.IntegerField()

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model=Employeedb
#         fields=['name','email','age','salary']

# class contact(forms.Form):
#     name=forms.CharField(max_length=100)
#     email=forms.EmailField()
#     message=forms.CharField(widget=forms.Textarea)

class contact(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','message']
