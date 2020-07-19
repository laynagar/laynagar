from django import forms 
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        to = ['nagarl@outlook.in']
        print(name,email)
        send_mail(subject,name+ " " + email + " " + message, 'layngr77@gmail.com', to)