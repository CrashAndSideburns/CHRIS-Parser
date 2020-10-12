import unittest
from context import chris

class TestParser(unittest.TestCase):

    def setUp(self):
        self.full = chris.parse('full.chris')
        self.no_date = chris.parse('no_date.chris')
        self.no_context = chris.parse('no_context.chris')
        self.no_date_context = chris.parse('no_date_context.chris')

    def test_quote(self):
        self.assertEqual(self.full.quote, 'full_quote')
        self.assertEqual(self.no_date.quote, 'nd_quote')
        self.assertEqual(self.no_context.quote, 'nc_quote')
        self.assertEqual(self.no_date_context.quote, 'ndc_quote')

    def test_last_name(self):
        self.assertEqual(self.full.author.last_name, 'full_ln')
        self.assertEqual(self.no_date.author.last_name, 'nd_ln')
        self.assertEqual(self.no_context.author.last_name, 'nc_ln')
        self.assertEqual(self.no_date_context.author.last_name, 'ndc_ln')

    def test_first_name(self):
        self.assertEqual(self.full.author.first_name, 'full_fn')
        self.assertEqual(self.no_date.author.first_name, 'nd_fn')
        self.assertEqual(self.no_context.author.first_name, 'nc_fn')
        self.assertEqual(self.no_date_context.author.first_name, 'ndc_fn')

    def test_year(self):
        self.assertEqual(self.full.date.year, '1970')
        self.assertIsNone(self.no_date.date.year)
        self.assertEqual(self.no_context.date.year, '1970')
        self.assertIsNone(self.no_date_context.date.year)

    def test_month(self):
        self.assertEqual(self.full.date.month, '1')
        self.assertIsNone(self.no_date.date.month)
        self.assertEqual(self.no_context.date.month, '1')
        self.assertIsNone(self.no_date_context.date.month)

    def test_day(self):
        self.assertEqual(self.full.date.day, '1')
        self.assertIsNone(self.no_date.date.day)
        self.assertEqual(self.no_context.date.day, '1')
        self.assertIsNone(self.no_date_context.date.day)

    def test_context(self):
        self.assertEqual(self.full.context, 'full_context')
        self.assertEqual(self.no_date.context, 'nd_context')
        self.assertIsNone(self.no_context.context)
        self.assertIsNone(self.no_date_context.context)

if __name__ == '__main__':
    unittest.main()