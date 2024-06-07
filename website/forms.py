from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255, required=False)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
