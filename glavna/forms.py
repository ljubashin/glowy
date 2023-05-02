from django import forms
from .models import komentari, Video,Category,Igdb

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

class videoupload(forms.ModelForm):
    title = forms.CharField(label=False,max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Write a title', 'class':'title-input'}))
    thumbnail = forms.ImageField(label=False,widget=forms.FileInput(attrs={'class':'dropzone image-input'}))
    video = forms.FileField(label=False,widget= forms.FileInput
                           (attrs={'class':'dropzone video-input', 'multiple': False}))
    description = forms.CharField(label=False,widget=forms.Textarea(attrs={'class': 'description-input','placeholder':'Write a description'}))
    category = forms.ModelChoiceField(label=False, queryset=Category.objects.all(),widget=forms.Select(attrs={"class":"category-input"})) 
    game = forms.ModelChoiceField(label=False, queryset=Igdb.objects.all(),widget=forms.Select(attrs={"class":"game-input"}))
    
    class Meta:
        model = Video
        fields = ['title', 'description', 'thumbnail', 'video','category', 'game']
        exclude = ("date","user", "slug")

        
