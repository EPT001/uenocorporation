from django import forms
from uenowebsite.models import Page, Category, Enquiry

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        help_text="Please enter the category name."
    )
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)
        
class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128,
        help_text="Please enter the title of the page."
    )
    url = forms.URLField(
        max_length=200,
        help_text="Please enter the URL of the page."
    )

    class Meta:
        model = Page
        exclude = ('category',)

class EnquiryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        help_text="Please enter your full name.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    company_name = forms.CharField(
        max_length=128,
        help_text="Please enter your company name.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        help_text="Please enter your email address.",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=15,
        help_text="Please enter your phone number.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    enquiry = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        required=False,
        help_text="Enter your enquiry details (optional)."
    )
    product_choice = forms.ChoiceField(
        choices=Enquiry.PRODUCT_CHOICES,
        help_text="Please select the product you're interested in.",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Enquiry
        fields = ('name', 'company_name', 'email', 'phone_number', 'enquiry', 'product_choice')
