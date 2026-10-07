from django import forms

class NameForm(forms.Form):
    Name = forms.CharField()
    Age = forms.IntegerField()
    Password = forms.CharField(widget=forms.PasswordInput)
    Gender = forms.ChoiceField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'),('OTHER', 'Other')],widget=forms.RadioSelect)
    Address = forms.CharField(widget=forms.Textarea)