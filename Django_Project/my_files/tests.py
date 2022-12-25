from django.test import TestCase
from django.urls import reverse
from .models import New

# Create your tests here.

class NewModelTest(TestCase):
     def setUp(self):
          New.objects.create(title="Title", text="News text")

     def test_text_content(self):
          new = New.objects.get(id=1)
          expected_object_title = f"{new.title}"
          expected_object_text = f"{new.text}"
          self.assertEqual(expected_object_title, "Title")
          self.assertEqual(expected_object_text, "News text")


class HomePageViewTest(TestCase):
     def setUp(self):
          New.objects.create(title="Title_2", text="Second New")

     def test_views_url_exists_at_proper_location(self):
          resp = self.client.get("/")
          self.assertEqual(resp.status_code, 200)

     def test_view_url_by_name(self):
          resp = self.client.get(reverse('home'))
          self.assertEqual(resp.status_code, 200)
          

     def test_view_uses_correct_template(self):
          resp = self.client.get(reverse('home'))
          self.assertEqual(resp.status_code, 200)
          self.assertTemplateUsed(resp, 'index.html')
