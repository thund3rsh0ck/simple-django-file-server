from django.shortcuts import render
from .models import PrivateFileUpload
from .models import PublicFileUpload
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'fileserver/index.html')

@login_required
def privatefilelist(request):
    private_file_list = PrivateFileUpload.objects.all()
    context = {'private_file_list': private_file_list}
    return render(request, 'fileserver/privatefilelist.html', context)

def publicfilelist(request):
    public_file_list = PublicFileUpload.objects.all()
    context = {'public_file_list': public_file_list}
    return render(request, 'fileserver/publicfilelist.html', context)
