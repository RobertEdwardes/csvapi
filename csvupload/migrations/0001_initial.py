# Generated by Django 4.0 on 2023-09-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='label_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mt_idx', models.IntegerField()),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='label_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mt_idx', models.IntegerField()),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='main_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('maj_tag_id', models.IntegerField()),
                ('min_tag_id', models.IntegerField()),
                ('uploaded_csv', models.JSONField()),
            ],
        ),
    ]
