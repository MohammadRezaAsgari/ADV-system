from django import forms


class AddAdvForm(forms.Form):
    ad_id = forms.IntegerField()
    img = forms.URLField()
    title = forms.CharField(max_length=250)
    site = forms.URLField()
