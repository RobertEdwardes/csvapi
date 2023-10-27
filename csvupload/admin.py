import csv
import json

from django import forms

from django.contrib import admin, messages
from django.urls import path, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import label_tag, label_group, main_table

import logging

logger = logging.getLogger('file')
# Register your models here.

admin.site.register(label_tag)
admin.site.register(label_group)

class CsvImport(forms.Form):
    csv_upload =forms.FileField()

class mainTableAdmin(admin.ModelAdmin):
    list_display = ('name','meta_details','group_id','maj_tag_id','min_tag_id')
    exclude = ('uploaded_csv',)
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
        
    def upload_csv(self, request):
        
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
                
            csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
            CF_NAME = csv_file.name
            header = next(csv_data)
            JSON_DATA = [dict(zip(header, row)) for row in csv_data]
            json_file = main_table(name=CF_NAME, uploaded_csv=json.dumps(JSON_DATA))
            json_file.save()
            url = reverse('admin:index')
            return HttpResponseRedirect(url) 
        
        form = CsvImport()
        data = {"form":form}
        return render(request, 'admin/csv_upload.html', data)
    
admin.site.register(main_table, mainTableAdmin)

