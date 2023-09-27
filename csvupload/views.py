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
                    'Get_File_By_Name': 'NOT IMPLEMENTED',
                    'Get_File_By_Index': 'NOT IMPLEMENTED',
                    'Get_By_Group': 'NOT IMPLEMENTED'
                    }
                }
            }
        }

def Most_Recent_5(request):
    recent_records = main_table.objects.order_by('-id')[:5].values()
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


def index(request):
    
    return JsonResponse(index_data)
    