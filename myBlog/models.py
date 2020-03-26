from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, verbose_name="Заголовок")
	description = models.TextField(blank=True, null=True, verbose_name="Аннотация")
	text = RichTextUploadingField(verbose_name="Текст")
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	

	def publish(self):
		#self.published_date = timezone.now()
		#self.save()
		pass

	class Meta():
		verbose_name = "Статьи"

	def __str__(self):
		return self.title