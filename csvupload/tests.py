from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import LiveServerTestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import time

from csvupload.models import main_table, label_group, label_tag

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

    def test_insert_tag_str_into_database(self):
        tag_str = 'tag_test'

        my_model_instance = label_tag(label=tag_str)
        my_model_instance.save()

        saved_instance = label_tag.objects.get(id=my_model_instance.id)

        self.assertEqual(saved_instance.label, tag_str)

class FileUploadTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_csv_insert_post(self):
        c = Client()

        login_successful = c.login(username='testuser', password='testpassword')

        self.assertTrue(login_successful, "User login failed")

        with open('test_data.csv', 'rb') as fp:
            response = c.post("/admin/csvupload/upload-csv/",{"csv_upload": fp}, follow=True)

        self.assertEqual(response.status_code, 200)

class LiveUiTesting(LiveServerTestCase):
    fixtures = ['user-data.json']
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get(f"{self.live_server_url}/admin/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("user1")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("password1")
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()