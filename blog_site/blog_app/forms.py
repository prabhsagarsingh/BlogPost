from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea) 

class CommentForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    body = forms.CharField(max_length=180)    