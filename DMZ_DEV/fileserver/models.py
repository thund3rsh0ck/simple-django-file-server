from django.db import models

class PrivateFileUpload(models.Model):
	privatefileuploaded = models.FileField(upload_to='privatefiles/%Y/%m/%d')
	def __str__(self):
		return str(self.privatefileuploaded)
