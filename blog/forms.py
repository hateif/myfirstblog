from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


from django.forms import ModelForm
from .models import ExamInfo
class ExamInfoForm(ModelForm):
    class Meta:
        model = ExamInfo
        fields = '__all__'


class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()



#---------------------------Programming the Django application
from django.forms import ModelForm
from .models import Input
class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
