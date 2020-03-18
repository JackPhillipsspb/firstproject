from django import forms

from .models import Post, SubscribeForm

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

class SubscribeForm(forms.ModelForm):

	class Meta:
		model = SubscribeForm
		fields = ('name', 'email',)


