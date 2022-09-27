from socket import fromshare
from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):   #define a class called 'TopicForm' which inherits from foorms.ModelForm
    class Meta:
        model = Topic               #build a form from the topic model
        fields = ['text']           #include only the text field
        labels = {'text': ''}       #this tells django NOT to generate a label for the text field

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'} #We again give the field 'text' a blank label
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
                                    #widget is an HTML form element, such as a single-line text box, multi-line
                                    #  text area, or drop-down list. By including the widgets attribute, you can
                                    #  override Django’s default widget choices. By telling Django to use a forms.
                                    # Textarea element, we're customizing the input widget for the field "text" to be 80 columns wide.