from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class SubscribeForm(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	subscribe_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.subscribe_date = timezone.now()
		self.save

	def __str__(self):
		return self.name

	class Meta():
		db_table = "Подпичсики"
		verbose_name = "Подписчики"


class zForm(models.Model):
    name = models.CharField(max_length=128, verbose_name="Имя", null=True, blank=True)
    email = models.CharField(verbose_name='email', max_length=256, null=True, blank=True)
    subject = models.CharField(max_length=128, verbose_name="Тема", null=True, blank=True)
    message = models.TextField(max_length=2056, verbose_name="Сообщение", null=True, blank=True)
    date_pub_forms = models.DateTimeField(null=True, blank=True, verbose_name="Дата сообщения")
    
    def publish(self):
    	self.date_pub_forms = timezone.now()
    	self.save()

    def __str__(self):
        return self.name

    class Meta():
        db_table = "Форма связи"
        verbose_name = "Форма связи"