
from django import forms

def validate_gmail_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise forms.ValidationError("This field accepts mail id of google only")
 

class MySampleForm(forms.Form):
    title = forms.CharField(max_length=5)
    description = forms.CharField(max_length=10,min_length=5,validators=[validate_gmail_mail])
    my_hobby = forms.ChoiceField(
        choices=(
            ('dance', 'Dance'),
            ('reading', 'Reading'),
        )
    )

