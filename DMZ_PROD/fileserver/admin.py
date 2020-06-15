from django.contrib import admin

from .models import PrivateFileUpload 
from .models import PublicFileUpload 

admin.site.register(PrivateFileUpload)
admin.site.register(PublicFileUpload)
