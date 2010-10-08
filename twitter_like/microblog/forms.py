from django.forms import ModelForm

from twitter_like.microblog.models import Tweet

class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['message']
