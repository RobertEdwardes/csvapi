# Generated by Django 4.0 on 2023-09-27 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csvupload', '0005_alter_label_group_options_alter_label_tag_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_table',
            name='alis_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='main_table',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='GroupTag', to='csvupload.label_group'),
        ),
        migrations.AlterField(
            model_name='main_table',
            name='maj_tag_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='MajorTag', to='csvupload.label_tag'),
        ),
        migrations.AlterField(
            model_name='main_table',
            name='meta_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='main_table',
            name='min_tag_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='MinorTag', to='csvupload.label_tag'),
        ),
    ]
