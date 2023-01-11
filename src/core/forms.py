from django import forms

from .models import Contact


class NewsLetterForm(forms.Form):
    email = forms.CharField(max_length=50)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        labels = {
            "name": "",
            "email": "",
            "message": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control', "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": 'form-control', "placeholder": "Email"}),
            "message": forms.Textarea(attrs={"class": 'form-control', "style": "height: 100px; margin-top:12px;", "placeholder": "Message"}),
        }