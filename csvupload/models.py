from django.db import models

# Create your models here.
    
class label_group(models.Model):
    label = models.CharField(max_length=255)
    
    class Meta: 
        verbose_name = ('Group')
        
    def __str__(self):
        return self.label
  
class label_tag(models.Model):
    label = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = ('Tag')
    
    def __str__(self):
        return self.label
        
class main_table(models.Model):
    name = models.CharField(max_length=255)
    alias_name = models.TextField(null=True, blank=True)
    meta_details = models.TextField(null=True, blank=True)
    group_id = models.ForeignKey(label_group, on_delete=models.PROTECT, null=True, blank=True, related_name='GroupTag')
    maj_tag_id = models.ForeignKey(label_tag, on_delete=models.PROTECT, null=True, blank=True, related_name='MajorTag')
    min_tag_id = models.ForeignKey(label_tag, on_delete=models.PROTECT, null=True, blank=True, related_name='MinorTag')
    uploaded_csv = models.JSONField()
    
    class Meta:
        verbose_name = ('Table')
    
    def __str__(self):
        return self.name