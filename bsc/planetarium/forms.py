from django import forms

class BlogPostForm(forms.Form):
    title = forms.CharField(label='Title')
    body = forms.TextField()
    slug = forms.SlugField()



