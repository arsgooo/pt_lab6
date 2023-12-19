import unittest
from flask_testing import TestCase
import pawnshop as ps

class TestGoodsFunctions(TestCase):

    def create_app(self):
        ps.app.config['TESTING'] = True
        return ps.app

    def setUp(self):
        self.app = self.app.test_client()
        ps.goods = {"Radio": 200, "Headphones": 300, "Watch": 499.55555, "Ring": 749.47755}

    def test_index_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Radio', response.data)
        self.assertIn(b'Headphones', response.data)
        self.assertIn(b'Watch', response.data)
        self.assertIn(b'Ring', response.data)

    def test_add_good_route(self):
        data = {'name': 'Laptop', 'price': 1000}
        response = self.client.post('/add_good', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Laptop', response.data)

    def test_remove_good_route(self):
        data = {'name': 'Radio'}
        response = self.client.post('/remove_good', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Radio', response.data)

    def test_get_goods_amount_route(self):
        response = self.client.get('/get_goods_amount')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Total number of goods: 4')

    def test_get_total_cost_route(self):
        response = self.client.get('/get_total_cost')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Total cost of goods: $1749.03', response.data)

if __name__ == '__main__':
    unittest.main()
