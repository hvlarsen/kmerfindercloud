from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
def handle_uploaded_file(f):
    with open('kmerfinder/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)