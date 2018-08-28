from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2015, 2036)]

    credit_card_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CARD NUMBER',
                                                                       'class': 'form-control-override'}),
                                         required=False)
    cvv = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CVV',
                                                        'class': 'form-control-override'}),
                          required=False)
    expiry_month = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control-override'}),
                                     choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control-override'}),
                                    choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'NAME ON CARD',
                                                       'class': 'form-control-override'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'PHONE NUMBER',
                                                                 'class': 'form-control-override'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'COUNTRY',
                                                            'class': 'form-control-override'}))
    postcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ZIP CODE',
                                                             'class': 'form-control-override'}))
    town_or_city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CITY',
                                                                 'class': 'form-control-override'}))
    street_address_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'BILLING ADDRESS',
                                                                     'class': 'form-control-override'}))
    street_address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'BILLING ADDRESS',
                                                                     'class': 'form-control-override'}))
    county = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'COUNTY',
                                                           'class': 'form-control-override'}))

    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode',
                  'town_or_city', 'street_address_1', 'street_address_2',
                  'county')
