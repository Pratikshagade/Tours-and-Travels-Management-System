from django.test import TestCase
from .models import Hotel
from django.core.files.uploadedfile import SimpleUploadedFile

class HotelIntegrationTest(TestCase):

    def setUp(self):
        self.image = SimpleUploadedFile(
            name="test_hotel.jpg",
            content=b"this is image",
            content_type="image/jpeg"
        )

        self.hotel = Hotel.objects.create(
            name="Test Hotel",
            description="A test hotel description",
            image=self.image
        )

    def test_hotel_creation(self):
        self.assertEqual(self.hotel.name, "Test Hotel")
        self.assertEqual(self.hotel.description, "A test hotel description")



    