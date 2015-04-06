from django import forms
from card.models import Card


class CardAdminForm(forms.ModelForm):
    model = Card

    card_id = forms.CharField(label='Card id', min_length=16, max_length=16)
    pin = forms.CharField(widget=forms.PasswordInput(), label='Pin code', min_length=4)
    balance = forms.DecimalField(max_digits=8, decimal_places=2)


class CardInputForm(forms.Form):
    card_id = forms.CharField(label='Card id', min_length=16, max_length=16, widget=forms.HiddenInput())


class CardPinInputForm(forms.Form):
    pin = forms.CharField(label='Pin code', min_length=4, max_length=8, widget=forms.PasswordInput())


class GetCashInputForm(forms.Form):
    amount = forms.IntegerField(label='Amount', min_value=10, widget=forms.HiddenInput())
