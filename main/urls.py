from django.urls import path
from .views import home, post, detail, delete, update, my_post


# router links
urlpatterns = [
    path('', home, name='home'),
    path('post/', post, name='post'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
    path('mypost/', my_post, name='mypost'),
]
