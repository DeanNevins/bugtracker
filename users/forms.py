from django import forms
from django.forms.widgets import PasswordInput, TextInput

class LoginForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={'class': 'nes-input'}), max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'nes-input'}))


class EmployeeForm(forms.Form):
    ADA = "/icons/ada.png"
    BODVAR = "/icons/bodvar.png"
    CASSIDY = "/icons/cassidy.png"
    GNASH = "/icons/gnash.png"
    HATTORI = "/icons/hattori.png"
    LORD_VRAXX = "/icons/lord_vraxx.png"
    ORION = "/icons/orion.png"
    QUEEN_NAI = "/icons/queen_nai.png"
    SCARLET = "/icons/scarlet.png"
    SENTINEL = "/icons/sentinel.png"
    SIR_ROLAND = "/icons/sir_roland.png"
    THATCH = "/icons/thatch.png"
    WU_SHANG = "/icons/wu_shang.png/"
    AVATAR_CHOICES = [
        (ADA, "Ada"),
        (BODVAR, "Bodvar"),
        (CASSIDY, "Cassidy"),
        (GNASH, "Gnash"),
        (HATTORI, "Hattori"),
        (LORD_VRAXX, "Lord Vraxx"),
        (ORION, "Orion"),
        (QUEEN_NAI, "Queen Nai"),
        (SCARLET, "Scarlet"),
        (SIR_ROLAND, "Sir Roland"),
        (THATCH, "Thatch"),
        (WU_SHANG, "Wu Shang"),
    ]
    username = forms.CharField(widget=TextInput(attrs={'class': 'nes-input'}), max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'nes-input'}))
    displayname = forms.CharField(widget=TextInput(attrs={'class': 'nes-input'}), max_length=30)
    avatar = forms.ChoiceField(widget=forms.Select(attrs={'class':'nes-input'}), choices = AVATAR_CHOICES)
    position = forms.CharField(widget=TextInput(attrs={'class': 'nes-input'}), max_length=150, required=False)
    first_name = forms.CharField(widget=TextInput(attrs={'class': 'nes-input'}), max_length=150, required=False)
    last_name = forms.CharField(widget=TextInput(attrs={'class': 'nes-input'}), max_length=150, required=False)
    email = forms.EmailField(widget=TextInput(attrs={'class': 'nes-input'}), required=False)