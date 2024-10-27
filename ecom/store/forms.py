from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UpdateUserForm(UserChangeForm):
    password = None

    email = forms.EmailField(
        label="📧 Email:",
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',
            'placeholder': 'Email Address',
            'style': 'padding-left: 30px;',
        })
    )
    first_name = forms.CharField(
        label="🧑 First Name:",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': 'First Name',
            'style': 'padding-left: 30px;',
        })
    )
    last_name = forms.CharField(
        label="🧑 Last Name:",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': 'Last Name',
            'style': 'padding-left: 30px;',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        # Username field customization
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-2 rounded-pill',
            'placeholder': 'User Name',
            'style': 'padding-left: 30px;',
        })
        self.fields['username'].label = '👤User Name:'
        self.fields['username'].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. '
            'Letters, digits, and @/./+/-/_ only.</small></span>'
        )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',  # Adds spacing and rounded edges
            'placeholder': '📧 Email Address',           # Adds an icon before the placeholder
            'style': 'padding-left: 30px;',             # Creates space for icon
        })
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🧑 First Name',
            'style': 'padding-left: 30px;',
        })
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🧑 Last Name',
            'style': 'padding-left: 30px;',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        # Username field customization
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-3 mt-3 rounded-pill',
            'placeholder': '👤 User Name',
            'style': 'padding-left: 30px;',
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. '
            'Letters, digits, and @/./+/-/_ only.</small></span>'
        )

        # Password1 field customization
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🔒 Password',
            'style': 'padding-left: 30px;',
        })
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>It should include both uppercase and lowercase letters.</li>'
            '<li>It can\'t be too similar to your other personal information.</li>'
            '<li>It can\'t be a commonly used password.</li>'
            '</ul>'
        )

        # Password2 field customization
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🔒 Confirm Password',
            'style': 'padding-left: 30px;',
        })
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        )
