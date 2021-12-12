from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, fields

class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True)
    username.widget.attrs.update({'class':'input', 'required':'required'})
    email = forms.EmailField(required=True)
    email.widget.attrs.update({'class':'input', 'required':'required'})
    password1 = forms.CharField(widget=PasswordInput)
    password1.widget.attrs.update({'class':'input', 'required':'required'})
    password2 = forms.CharField(widget=PasswordInput)
    password2.widget.attrs.update({'class':'input', 'required':'required'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # email = forms.EmailField(required=True)
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']
    #     widgets = {
    #         'username': TextInput(attrs={
    #             'class': "input",
    #         }),
    #         'email': EmailInput(attrs={
    #             'class': "input",
    #         }),
    #         'password1': PasswordInput(attrs={
    #             'class': "input",
    #         }),
    #         'password2': PasswordInput(attrs={
    #             'class': "input",
    #         }),
    #     }

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2") # first_name, last_name
    
#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         # user.first_name = self.cleaned_data['first_name']
#         # user.last_name = self.cleaned_data['last_name']
#         if commit:
#             user.save()
#         return user