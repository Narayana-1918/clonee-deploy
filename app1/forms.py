from django import forms
from .models import *
from django.contrib.auth.hashers import make_password

class UserForm(forms.ModelForm):
    class Meta:
        model=New_user
        fields=['username','first_name','last_name','password','phone_no','email']

    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        print(self.cleaned_data)
        s.save()
        return s
    
    def clean_username(self):
        iuname=self.cleaned_data['username']
        if len(iuname)<5:
            raise forms.ValidationError('should be of length 5 or above')
        return iuname

class UserloginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())

class AddetailForm(forms.ModelForm):
    class Meta:
        model=Delivery_details
        fields='__all__'

    # def save(self):
    #     s=super().save(commit=False)
    #     s.password=make_password(self.cleaned_data['password'])
    #     s.save()
    #     return s
