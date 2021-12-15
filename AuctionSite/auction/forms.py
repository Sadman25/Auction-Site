from django import forms
from django.contrib.auth import models
from django.db.models import fields
from .models import product, images, bidding
from django.contrib.admin.widgets import AdminSplitDateTime



class productForm(forms.ModelForm):
    product_description = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':30}))
    deadline = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    class Meta:
        model = product
        fields = ['product_category','product_name','product_description','starting_bid','deadline','cover_photo','product_status']


class imagesForm(forms.ModelForm):
    class Meta:
        model = images
        fields = ['image']

class biddingForm(forms.ModelForm):

    class Meta:
        model = bidding
        fields = ['bid']