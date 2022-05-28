
from django import forms
from todo.models import Todo
def validate_gmail_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise forms.ValidationError("This field accepts mail id of google only")
 

class MySampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500,validators=[],widget=forms.Textarea)
    my_hobby = forms.ChoiceField(
        choices=(
            ('dance', 'Dance'),
            ('reading', 'Reading'),
        )
    )

class MyTodoForm(forms.ModelForm):
     class Meta:
        model = Todo
        fields = "__all__"

