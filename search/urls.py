from django.urls import path

from .views import searchposts

# app_name = 'search'

urlpatterns = [
	path('search/', searchposts, name='searchposts'),
]    
