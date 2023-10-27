from django.test import TestCase
import csv
from csvupload.models import main_table, label_group

class DataBaseTest(TestCase):
    def test_insert_json_into_database(self):
        json_data = [{"key1": "value1", "key2": "value2"},{"key1": "value1", "key2": "value2"}]

        my_model_instance = main_table(name='test_data',uploaded_csv=json_data)
        my_model_instance.save()

        saved_instance = main_table.objects.get(id=my_model_instance.id)

        self.assertEqual(saved_instance.uploaded_csv, json_data)

    def test_insert_label_str_into_database(self):
        label_str = 'label_test'
        my_model_instance = label_group(label=label_str)
        my_model_instance.save()

        saved_instance = label_group.objects.get(id=my_model_instance.id)

        self.assertEqual(saved_instance.label, label_str)

class FileUploadTest(TestCase):
    def test_csv_insert_post(self):
        c = self.client

        with open('test_data.csv', 'rb') as fp:
            response = c.post("/admin/csvupload/upload-csv/",{"csv_upload": fp})

        self.assertEqual(response.status_code, 200) 