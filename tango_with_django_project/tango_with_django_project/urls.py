from django.contrib import admin
from django.urls import path,include
from Rango import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
	def get_success_url(self, user):
		print("shukar hai!")
		return '/add_profile/'

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('Rango.urls')),
	path('accounts/register/',MyRegistrationView.as_view(),name='registration_register'),
	path('accounts/',include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
