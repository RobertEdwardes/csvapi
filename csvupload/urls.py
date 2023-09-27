# urls.py
from django.urls import path
from .views import index, Most_Recent_5,Tag_list, Group_list

urlpatterns = [
   path('', index, name='index'),
   path('Most_Recent_5', Most_Recent_5,  name='Most_Recent_5'),
   path('Tag_list', Tag_list,  name='Tag_list'),
   path('Group_list', Group_list,  name='Group_list')
]