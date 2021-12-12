from django import forms
from django.contrib.auth import models
from django.db.models import fields
from .models import product, images
from django.contrib.admin.widgets import AdminSplitDateTime



class productForm(forms.ModelForm):
    product_description = forms.CharField(widget=forms.Textarea)
    deadline = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    class Meta:
        model = product
        fields = ['product_name','product_description','starting_bid','deadline','cover_photo']


class imagesForm(forms.ModelForm):
    class Meta:
        model = images
        fields = ['image']