from django.test import TestCase

# Create your tests here.

def test_hello_view(self):
    response = self.client.get('/hello/')
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Hello World!')