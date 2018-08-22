from django import forms

from .models import Post, Topic, PARKING_SMALL_CHOICES


class NewTopicForm(forms.ModelForm):
    message = forms.ChoiceField(choices=PARKING_SMALL_CHOICES)
    image_address = forms.CharField(max_length=255, help_text='The image should be stored at static/img/')
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Description of the parking lot'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )
    class Meta:
        model = Topic
        fields = ['subject', 'message', 'description', 'image_address']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
        labels = {'message': "Post your update"}
