from djongo import models
from django.forms import ModelForm


# Create your models here.
class Sugestion(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()

class SugestionForm(ModelForm):
    class Meta:
        model = Sugestion
        fields = ['name', 'email', 'message']
