from django import forms
from django.db import models
from issue.models import *

class complaintform(forms.ModelForm):
    class Meta:
        model=complaint
        fields='__all__'