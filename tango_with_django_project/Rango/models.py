from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	likes= models.IntegerField(default=0)
	views= models.IntegerField(default=0)
	slug = models.SlugField(unique =True)

	class Meta:
		verbose_name_plural='Categories'

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		print(self.slug)
		super(Category,self).save(*args,**kwargs)

	def __str__(self):
		return self.name


		
class Page(models.Model):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete="models.CASCADE")

	picture = models.ImageField(upload_to='profile_images',blank=True)
	website = models.URLField(blank=True)

	class Meta:
		verbose_name = "UserProfile"
		verbose_name_plural = "UserProfiles"

	def __str__(self):
		return self.user.username 