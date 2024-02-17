# import unittest 
# from unittest.mock import patch
# from  simple_ordering_system.system_components import * 

# class TestOderingSystemTests(unittest.TestCase):

#     def __init__(self):
#         # self.menu = menu.Menu()
#         # self.order = Order()
#         pass

#     def setUp(self):

#         self.mock_order = [
#             {"name": "cake","price":2.79},
#             {"name": "coffee","price": 2.50}
#             ]
        
#         self.mock_subtotal = calculate_subtotal(self.mock_order)
#         self.mock_tax = round((self.mock_subtotal *15)/100,2)
#         self.mock_total = round((self.mock_subtotal + self.mock_tax),2)


#     @patch("ordering_system.calculate_subtotal")
#     def test_calculate_subtotal(self, mock_calculate_subtotal):
#         output = calculate_subtotal(self.mock_order)
#         self.assertEqual(output, self.mock_subtotal)
        

#     @patch("ordering_system.calculate_tax")
#     def test_calculate_tax(self, mock_calculate_tax):

        
#         output = calculate_tax(self.mock_subtotal)
#         self.assertEqual(output, self.mock_tax)
       
        
#     @patch("ordering_system.summarize_order")
#     def test_summarize_order(self, mock_summarize_order):
        
#         mock_names = [mock_item["name"] for mock_item in self.mock_order]
#         mock_order_summary = (mock_names, self.mock_total)
#         output = summarize_order(self.mock_order)
#         self.assertEqual(output, mock_order_summary)

# if __name__ == "__main__":
#     unittest.main()