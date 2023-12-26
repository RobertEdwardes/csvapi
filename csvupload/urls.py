# urls.py
from django.urls import path
from .views import index, Most_Recent_5,Tag_list, Group_list, get_by_name, get_by_alias, get_by_index, get_by_group, json_doc

urlpatterns = [
   path('', index, name='index'),
   path('json_doc', json_doc, name='json_doc'),
   path('Most_Recent_5', Most_Recent_5,  name='Most_Recent_5'),
   path('Tag_list', Tag_list,  name='Tag_list'),
   path('Group_list', Group_list,  name='Group_list'),
   path('name/<str:input_str>/', get_by_name, name='get_by_name'),
   path('alias/<str:input_str>/', get_by_alias, name='get_by_alias'),
   path('idx/<int:input_int>/', get_by_index, name='get_by_index'),
   path('group/<int:input_int>/', get_by_group, name='get_by_group'),
]