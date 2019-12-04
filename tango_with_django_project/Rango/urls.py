from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('profiles/',views.list_profiles,name='list_profiles'),
	path('profiles/<slug:username>/',views.profile,name="profile"),
	path('add_profile/',views.register_profile,name="add_profile"),
	path('category/<slug:category_name_slug>/',views.show_category,name='show_category'),
	path('add_category/',views.add_category, name= 'add_category'),
	path('category/<slug:category_name_slug>/add_page/',views.add_page, name='add_page' ),
	path('goto/',views.track_url , name = 'goto'),
	path('suggest/',views.suggest_category,name='suggestion'),
	path('like_category/',views.like_category,name="like_category"),
	path('add/',views.auto_add_page,name="auto_add_page"),
]