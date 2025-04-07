from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ContactUs, Comments
from django.core.validators import RegexValidator


#convert email and other fields to lowercase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()

class Capitalize(forms.CharField):
    def to_python(self, value):
        return value.capitalize()

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email...'}),
                            label=False,
                            )
    
    field_order = ['username','email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remove default help text
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
        # Remove field labels
        self.fields['password1'].label = False
        self.fields['password2'].label = False
        self.fields['username'].label = False
        
        # Add placeholders
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Your Password...'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password...'
        self.fields['username'].widget.attrs['placeholder'] = 'Username...'
        
        # Customize error messages
        self.fields['username'].error_messages = {
            'required': 'Please enter a username.',
            'max_length': 'Username cannot exceed 150 characters.',
            'unique': 'This username is already taken.',
            # Add more custom error messages as needed
        }
        self.fields['password1'].error_messages = {
            'required': 'Custom password field required message',
            
            # Add more custom error messages as needed
        }
        self.fields['password2'].error_messages = {
            'required': 'Please confirm your password.',
            'min_length': 'Password must be at least 8 characters long.',
            'password_mismatch': 'Passwords do not match.',
            # Add more custom error messages as needed
        }
        
class ContactForm(forms.ModelForm):
#VALIDATION
    name = Capitalize(
        label='Name',min_length=5,max_length=200,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$',
        message = "Only letters are allowed")],
        widget=forms.TextInput(attrs={
                                        'placeholder': 'Enter your name...',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0, border: 10px solid #0f0f0f',
                                        }
                                )
    )
    email = Lowercase(
        label='Email Address',min_length=10,max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message = "Put a valid email address"
        )],
        widget=forms.TextInput(attrs={
                                        'placeholder': 'Enter your Email Address...',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                    }
                                ),
    )

    subject = forms.CharField(
        label='Subject',min_length=5,max_length=200,
        validators=[RegexValidator(r'^[a-zA-Z\s.-_]*$',
        message = "Only letters are allowed!")],
        widget=forms.TextInput(attrs={
                                        'placeholder': 'Subject....',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                        }
                                ),
        required=False
    )
    contactNumber = forms.CharField(
        label='Phone Number', min_length=7,max_length=200,
        validators=[RegexValidator(r'^[0-9]',
        message = "Only digits are allowed!")],
        widget=forms.TextInput(attrs={
                                        'placeholder': 'Enter Your Phone Number....',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                        }
                                ),
        required=False
    )
    
    message = forms.CharField(
        label='message',min_length=20, max_length=1000,
        widget=forms.Textarea(attrs={
                                        'placeholder': 'Type a Message ...',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                        'rows':4
                                    }
                            )
    )
    class Meta:
        model = ContactUs
        fields = ['name', 'email','contactNumber', 'subject', 'message']

class CommentForm(forms.ModelForm):
    message = forms.CharField(
        label='Comment', max_length=1000,
        widget=forms.Textarea(attrs={
                                        'placeholder': 'Type Your Comment ...',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                        'rows':4,
                                    }
                            )
    )
    class Meta:
        model = Comments

        fields = ['message', ]

        fields = ['message', ]

