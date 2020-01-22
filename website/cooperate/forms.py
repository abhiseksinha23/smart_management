from django import forms
from .models import centers, faculties, fee, quaries, rankers, students

class centersform(forms.Modelform):
    class meta():
        model = quaries
        fields = '__all__'

class facultiesform(forms.ModelForm):
    class meta():
        model = faculties
        fields = '__all__'
        

class feeform(forms.ModelForm):
    class meta():
        model = fee
        fields = '__all__'

class studentsform(forms.ModelForm):
    class meta():
        model = students
        fields = '__all__'

class rankersform(forms.ModelForm):
    class meta():
        model = rankers
        fields = '__all__'

class quariesform(forms.ModelForm):
    class meta():
        model = quaries
        fields = '__all__'
