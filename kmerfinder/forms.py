from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
	
class UploadFileForm(forms.Form):
    enctype="multipart/form-data"
    file = forms.FileField(label="FILE")