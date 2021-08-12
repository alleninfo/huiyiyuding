from datetime import date

from django import forms
import re

from django.forms import DateInput


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.'?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()



class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    org = forms.CharField(label='Organization', max_length=50, required=False)
    telephone = forms.CharField(label='Telephone', max_length=50, required=False)


class PwdChangeForm(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)

    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    # use clean methods to define custom validation rules

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("your password is too long")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch Please enter again")

        return password2


class applymeeting(forms.Form):
    meetingname = forms.CharField(label='meeting', max_length=100)
    start_date = forms.DateField(initial=date.today().replace(),
                                 label='开始时间', widget=DateInput(format='%Y-%m-%d %H:%M:%S'),
                                 input_formats=['%Y-%m-%d %H:%M:%S'])
    end_date = forms.DateField(initial=date.today().replace(),
                                 label='结束时间', widget=DateInput(format='%Y-%m-%d %H:%M:%S'),
                                 input_formats=['%Y-%m-%d %H:%M:%S'])
    applyname = forms.CharField(max_length=100)