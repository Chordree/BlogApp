from django.urls import path
from . import views  # see if this should be here 

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:var>', views.post, name='postt'),
    path('add', views.addpost, name='addpost'),
]

