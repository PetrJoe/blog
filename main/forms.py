from django import forms
from .models import Post,Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', "placeholder": "Enter Post title"}),
            'text': forms.Textarea(
                attrs={'class': 'form-control z-depth-1', "placeholder": "Write Post here" })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Add Comment....", 'required': True, }),
        }
