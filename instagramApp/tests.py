from django.test import TestCase
from .models import Photo,tags

# Create your tests here.
class PhotoTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.photo= Photo(pub_date='2019',photo='null.png',likes=0,favorites=0)