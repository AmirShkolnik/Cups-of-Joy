from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import ContactForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about us content"""
        self.about_content = About(
            title="About Us", content="This is about us.")
        self.about_content.save()

    def test_render_about_page_with_Contact_form(self):
        """Verifies get request for about me containing a contact form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Us', response.content)
        self.assertIn(b'Contact Us!', response.content)
        self.assertIsInstance(
            response.context['form'], ContactForm)
