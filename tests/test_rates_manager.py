import unittest
from src import rates_manager

class TestMain(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass


	def test_formatResponse(self):
		base = "nzd"
		rates = {
			"aud": 0.9
		}
		sources = "Cache"
		expected = {
			"sources": "Cache",
			"base": "NZD",
			"rates": {
				"AUD": 0.9
			}
		}
		output = rates_manager.formatResponse(base, rates, sources)
		self.assertDictEqual(expected, output)


	def test_combineRates(self):
		rates1 = {
			"aud": 0.9,
			"usd": 0.3
		}
		rates2 = {
			"USD": 0.5
		}
		expected = {
			"AUD": 0.9,
			"USD": 0.4
		}
		output = rates_manager.combineRates(rates1, rates2)
		self.assertDictEqual(expected, output)


if __name__ == "__main__":
	unittest.main()