import unittest
import calculadora


class TestCalculadora(unittest.TestCase):

    def test_clicks_per_views_large(self):
        clicks = calculadora.get_clicks(200)
        self.assertEqual(clicks, 24)

    def test_clicks_per_views_small(self):
        clicks = calculadora.get_clicks(20)
        self.assertEqual(clicks, 2)

    def test_shares_per_click_large(self):
        shares = calculadora.get_shares_by_clicks(60)
        self.assertEqual(shares, 9)

    def test_shares_per_click_small(self):
        shares = calculadora.get_shares_by_clicks(10)
        self.assertEqual(shares, 1)

    def test_views_per_share(self):
        views = calculadora.get_views_by_share(2)
        self.assertEqual(views, 80)

    def test_views_per_share_zero(self):
        views = calculadora.get_views_by_share(0)
        self.assertEqual(views, 0)
