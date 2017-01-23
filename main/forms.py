from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Book


class AuthForm (AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        fields = ['username', 'password']
        # model = User


class RegistrationForm (UserCreationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
     
    class Meta:
        fields = ['username', 'password1', 'password2']
        model = User
        
        
class AddBookForm(forms.Form):
    name = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(
            attrs={'placeholder': 'Name', 'id': 'new_rec_name', 'maxlength': '49'}           
        ),
        error_messages={'required': 'Please enter a team name'},
        label='Team name'
    )
      
    author = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'placeholder': 'Author', 'id': 'new_rec_country', 'maxlength': '29'}
        )
    )
    
    genre = forms.CharField(required=True,
        widget=forms.widgets.TextInput(
            attrs={'placeholder': 'Genre', 'id': 'new_rec_sportType', 'maxlength': '29'}            
        ),
        error_messages={'required': 'Please input sport name'},
        label='Sport'
    )
    
    
    desc = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={'placeholder': 'Description', 'id': 'new_rec_desc', 'maxlength': '1999'}
        ),
        error_messages={'required': 'Please input short description'},
        label='Sport'
    )
    
    image = forms.FileField(required=False,
        widget=forms.widgets.ClearableFileInput(
            attrs={'accept':'image/jpeg, image/png, image/gif', 'id':'new_rec_img'}
        )
    )

    def fill_object(self):
        return Book.objects.create(
            name = self.cleaned_data['name'],
            author = self.cleaned_data['author'],
            genre = self.cleaned_data['genre'],
            desc = self.cleaned_data['desc']
        )
    
    
    