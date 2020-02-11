from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.test import Client
from django.urls import reverse

from .models import Peak


class PeakViewSetTestCase(TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        self.client.login(username='mfi', password='fguibert')

        self.name = 'Montcalivert'
        self.lat = 43.011
        self.lon = 1.164
        self.altitude = 677

        self.peak_test = {
          'name': self.name,
          'lat': self.lat,
          'lon': self.lon,
          'altitude': self.altitude,
        }

    def create_peak(self):
        response = self.client.post(reverse('peaks-list'), data=self.peak_test, content_type="application/json")
        return response

    def test_get(self):
        """Get the created peak."""
        self.create_peak()
        response = self.client.get(reverse('peaks-detail', kwargs={'name': self.name}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.name)

    def test_post(self):
        """Post to create a peak."""
        nb_before = Peak.objects.count()

        response = self.create_peak()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        nb_after = Peak.objects.count()
        self.assertEqual(nb_after, nb_before + 1)
