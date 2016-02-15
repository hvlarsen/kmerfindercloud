from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from kmerfinder.forms import UploadFileForm
from .models import handle_uploaded_file

# Create your views here.
def index(request):
    return render(request, 'kmerfinder/index.html')
	
def DetailView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadFileForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
    else:
        form = UploadFileForm()
    return render(request, 'kmerfinder/detail.html', {'form': form})
	