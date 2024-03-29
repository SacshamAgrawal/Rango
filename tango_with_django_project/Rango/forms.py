from django import forms 
from Rango.models import Category,Page , UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):

	name=forms.CharField( max_length=128 , help_text='Category Name')
	views= forms.IntegerField(widget=forms.HiddenInput(),initial = 0)
	likes= forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Category
		fields = {'name',}

class PageForm(forms.ModelForm):

	title = forms.CharField(max_length=128 , help_text='Please enter the title')
	url = forms.URLField(max_length=200 , help_text='enter url')
	views = forms.IntegerField( widget=forms.HiddenInput(),initial=0 )

	class Meta:
		model = Page
		exclude = {'category',}
    
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta : 
		model = User
		fields=('username','password','email')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')