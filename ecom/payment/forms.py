from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🧑 Full Name',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    shipping_email = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '📧 Email',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    shipping_address1 = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🏠 Address1',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    shipping_address2 = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🏠 Address1',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    shipping_city = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🏙️ City',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    shipping_state = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🗺️ State',
            'style': 'padding-left: 30px;',
        }), 
        required=False
    )
    shipping_zipcode = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '📬 Zipcode',
            'style': 'padding-left: 30px;',
        }), 
        required=False
    )
    shipping_country = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🌍 Country',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']

        exclude = ['user',]

class PaymentForm(forms.Form):
    card_name = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🧑 Name on Card',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    card_number = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '💳 Card Number',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    card_exp_date = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '📅 Expiration Date (MM/YY)',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    card_cvv_number = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🔒 CVV',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    card_address1 = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🏠 Billing Address1',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    card_address2 = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🏠 Billing Address2',
            'style': 'padding-left: 30px;',
        }), 
        required=False
    )
    card_city = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🏙️ City',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    card_zipcode = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '📬 Zipcode',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )
    card_country = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🌍 Country',
            'style': 'padding-left: 30px;',
        }), 
        required=True
    )