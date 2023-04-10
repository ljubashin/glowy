from django import forms
from .models import komentari

class komentariform(forms.ModelForm):
    class Meta:
        model = komentari
        exclude = ["video","date","user_name"]
        label = {
            "text": "Your Comment",
            "like": "Do you like this game"
        }
        widgets = {
            "text" : forms.Textarea(attrs={'class': "form__field"}),
            "like" : forms.RadioSelect(choices=((False,"No"),(True,"Yes")),attrs={'class': "boolean"})
        }