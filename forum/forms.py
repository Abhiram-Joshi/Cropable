from django import forms
from .models import *
 
class CreateInForum(forms.ModelForm):
    class Meta:
        model= forum
        fields = "__all__"

        widgets = {
            'discuss': forms.Textarea(),
        }
 
class CreateInDiscussion(forms.ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"

        widgets = {
            'discuss': forms.Textarea(),
        }