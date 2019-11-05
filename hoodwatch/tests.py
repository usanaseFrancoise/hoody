from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username = 'fanny', email = 'fanny@fanny.com', password = 'havugima')
        self.user.save()
        self.fanny = Profile(bio = 'A python Programmer', user = self.user)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.fanny,Profile))


class HoodTest(TestCase):
    def setUp(self):
        self.user = User(username='fanny', email='fanny@fanny.com', password='havugima')
        self.user.save()
        self.fanny = Profile(bio='A python Programmer', user=self.user)
        self.hood = Hood(name = 'jane',bio = "welcome",admin = self.user)

    def tearDown(self):
        Profile.objects.all().delete()