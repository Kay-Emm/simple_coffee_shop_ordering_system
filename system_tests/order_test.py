import unittest 
from unittest.mock import patch
from system_components.menu import *
from system_components.order import *


class TestSystemTests(unittest.TestCase):

   
    def setUp(self):
        self.menu = Menu()
        self.order = Order()

        self.mock_order = [
            {"name": "cake","price":2.79},
            {"name": "coffee","price": 2.50}
            ]
        
        self.mock_subtotal = self.order.calculate_subtotal(self.mock_order)
        self.mock_tax = round((self.mock_subtotal *15)/100,2)
        self.mock_total = round((self.mock_subtotal + self.mock_tax),2)
        # self.mock_amount_to_pay = self.order.prompt()

    @patch("system_components.order.Order.calculate_subtotal", return_value = 5.29)
    def test_calculate_subtotal(self, mock_calculate_subtotal):
        output = self.order.calculate_subtotal(self.mock_order)
        self.assertEqual(output, self.mock_subtotal)
        

    @patch("system_components.order.Order.calculate_tax", return_value = 0.79)
    def test_calculate_tax(self, mock_calculate_tax):
        
        output = self.order.calculate_tax(self.mock_subtotal)
        self.assertEqual(output, self.mock_tax)
       
        
    @patch("system_components.order.Order.summarize_order",return_value = (['cake', 'coffee'], 6.08))
    def test_summarize_order(self, mock_order_summary):
        
        mock_names = [mock_item["name"] for mock_item in self.mock_order]
        mock_order_summary = (mock_names, self.mock_total)
        output = self.order.summarize_order(self.mock_order)
        self.assertEqual(output, mock_order_summary)

    @patch("builtins.input", side_effect = ["7.08"])
    def test_calculate_change(self, mock_prompt):
       
        mock_change = round(float("7.08") - self.mock_total, 2)
        output = float(self.order.calculate_change(self.mock_total, mock_prompt))
        
        self.assertEqual(output, mock_change)
        

if __name__ == "__main__":
    unittest.main()