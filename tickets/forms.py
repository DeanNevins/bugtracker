from django import forms

class TicketAddForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'nes-input'}), max_length=150)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'nes-textarea'}))
