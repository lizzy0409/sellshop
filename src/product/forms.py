from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ["full_name", "email", "review", "rating"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": 'form-control', "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": 'form-control', "placeholder": "Email"}),
            "review": forms.Textarea(attrs={"class": 'form-control', "style": "height: 100px;", "placeholder": "Review"}),
            "rating": forms.Select(attrs={"class": "form-control"})
        }