from django import forms
from polls.models import Question
from django.core.files.uploadedfile import InMemoryUploadedFile
from ads.humanize import naturalsize

# Create the form class.
class CreateForm(forms.ModelForm):
    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = Question
        fields = ['answer']  # Picture is manual

    # Validate the size of the picture

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other

