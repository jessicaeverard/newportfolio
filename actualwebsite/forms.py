from django.forms import ModelForm, Textarea
from .models import Contact

class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
                            {'class': '.input-field'})

    class Meta:
        model = Contact
        fields = ['name','message', 'email']    
