from django import forms
from .models import Class1, Class2, Class3

class Class1Form(forms.ModelForm):
    class Meta:
        model = Class1
        fields = ('field1', 'field2')

class Class2Form(forms.ModelForm):
    class Meta:
        model = Class2
        fields = ('field1', 'field2')

class Class3Form(forms.ModelForm):
    class Meta:
        model = Class3
        fields = ('field1', 'field2')
