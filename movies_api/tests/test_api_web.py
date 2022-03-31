from django.test import TestCase
from movies_api.api_web import ApiWeb

class ApiWebTestCase(TestCase):

    def setUp(self):
        self.api_web = ApiWeb()

    def test_add_filters_url(self):
        """
        Should add filters to url
        """
        url = 'http://example.com'
        url_filters = 'http://example.com?search=item&order_by=name'
        filters = {'search':'item', 'order_by':'name'}
        url = self.api_web.add_filters_url(url, filters)
        self.assertEqual(url, url_filters)