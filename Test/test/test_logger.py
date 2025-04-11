import unittest
from unittest.mock import patch
from test.looger import notify_user
from test.additionfunc import add

class testaddition(unittest.TestCase):
    def test_add(self):
        result  = add(5, 5)
        self.assertEqual(result, 10)

    def test_add_negative_number(self):
        result = add(-5,-15)
        self.assertEqual(result,-20)


# class testlogger(unittest.TestCase): 
#     @patch('looger.log_message')
#     def test_notify(self,mock_log_message):
#         result = notify_user("Test message")
#         self.assertEqual(result, "Notification sent")

#         mock_log_message.assert_called_with("Test message")
#         self.assertEqual(mock_log_message.call_count,1)


if __name__ == '__main__':
    unittest.main()