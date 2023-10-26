from django.test import TestCase
from csvupload.models import main_table  # Import your model here

class DataBaseTest(TestCase):
    def test_insert_json_into_database(self):
        json_data = [{"key1": "value1", "key2": "value2"},{"key1": "value1", "key2": "value2"}]

        my_model_instance = main_table(json_data=json_data)
        my_model_instance.save()

        saved_instance = main_table.objects.get(id=my_model_instance.id)

        self.assertEqual(saved_instance.json_data, json_data)
