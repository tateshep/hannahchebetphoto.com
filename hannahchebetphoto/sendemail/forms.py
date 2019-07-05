from django import forms

class ContactForm(forms.Form):
    # Contact form fiedls used by the view
    
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
