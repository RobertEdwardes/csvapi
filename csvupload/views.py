from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from .models import main_table, label_tag, label_group
# Create your views here.
index_data = {
        'Intro': 'Welcome to the Index of the CSV to API demo',
        'Simple_Guide': {
            'API_General_Description':{
                'Schema':{
                    'Name':'File Name at Upload [CAN NOT Be Blank]',
                    'Meta_Description':'User generated description appened to the json independ of the data [Can be Blank]',
                    'GroupTag': 'Group Tag [Can be Blank]',
                    'MajorTag': 'Major Tag from List of Tags [Can Be Blank]',
                    'MinorTag': 'Minor Tag from List of Tags [Can Be Blank]',
                    'uploaded_csv': 'Record Oriented JSON [CAN NOT Be Blank ---- THIS IS THE WHOLE POINT ----]'
                }
            },
            'sample_urls':{
                'Static_Urls':{
                    'Groups': '/Group_list',
                    'Tags': '/Tag_list',
                    'Most_Recent_5':'/Most_Recent_5'
                    },
                'Url_Patterns':{
                    'Get_File_By_Name': 'name/<str:input_str>/',
                    'Get_File_By_Alias': 'alias/<str:input_str>/',
                    'Get_File_By_Index': 'idx/<int:input_int>/',
                    'Get_By_Group': 'group/<int:input_int>/'
                    }
                }
            }
        }

def Most_Recent_5(request):
    recent_records = main_table.objects.order_by('-id')[:5].values('name','alias_name','meta_details','group_id','maj_tag_id','min_tag_id')
    if len(recent_records) == 0:
        index_data['Status'] = '204 - Most_Recent_5 No Content'
        return JsonResponse(index_data, status=204, safe=False)
    return JsonResponse(list(recent_records), safe=False)
    
def Group_list(request):
    recent_records = label_group.objects.order_by('-id').values()
    if len(recent_records) == 0:
        index_data['Status'] = '204 - Group_list No Content'
        return JsonResponse(index_data, status=204, safe=False)
    output = {i['id']: i['label'] for i in list(recent_records)}
    return JsonResponse(output, safe=False)
 
def Tag_list(request):
    recent_records = label_tag.objects.order_by('-id').values()  
    if len(recent_records) == 0:
        index_data['Status'] = '204 - Tag_list No Content'
        return JsonResponse(index_data, status=204, safe=False)
    output = {i['id']: i['label'] for i in list(recent_records)}
    return JsonResponse(output, safe=False)
    
    
def get_by_name(request, input_str):
    recent_records = main_table.objects.filter(name=input_str).values()
    if len(recent_records) == 0:
        index_data['Status'] = '204 - No Content For File Name'
        return JsonResponse(index_data, status=204, safe=False)
    return JsonResponse(list(recent_records), safe=False)
    
def get_by_alias(request, input_str):
    recent_records = main_table.objects.filter(alias_name=input_str).values()
    if len(recent_records) == 0:
        index_data['Status'] = '204 - No Content For Alias Name'
        return JsonResponse(index_data, status=204, safe=False)
    return JsonResponse(list(recent_records), safe=False)
    
def get_by_index(request, input_int):
    recent_records = main_table.objects.filter(id=input_int).values()
    if len(recent_records) == 0:
        index_data['Status'] = '204 - No Content For Index'
        return JsonResponse(index_data, status=204, safe=False)
    return JsonResponse(list(recent_records), safe=False)
    
def get_by_group(request, input_int):
    recent_records = main_table.object.filter(group_id=input_int).values()
    if len(recent_records) == 0:
        index_data['Status'] = '204 - No Content For Group ID'
        return JsonResponse(index_data, status=204, safe=False)
    return JsonResponse(list(recent_records), safe=False)


def index(request):
    
    return JsonResponse(index_data)
    