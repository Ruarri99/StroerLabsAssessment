import unittest
from src import cache_handler

class TestMain(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		pass


	@classmethod
	def tearDownClass(cls):
		pass


	def test_checkCacheValid(self):
		cache = {
			"NZD": {
				"AUD": 0.9
			}
		}
		expected = {
			"sources": "Cache",
			"base": "NZD",
			"rates": {
				"AUD": 0.9
			}
		}
		output = cache_handler.checkCache(cache, "NZD", ["AUD"])
		self.assertDictEqual(output, expected)


	def test_checkCacheInvalid(self):
		cache = {
			"NZD": {
				"AUD": 0.9
			}
		}
		output = cache_handler.checkCache(cache, "USD", ["AUD"])
		self.assertListEqual(output, [])


	def test_formatCache(self):
		cache = {
			"base": "NZD",
			"rates": {
				"AUD": 0.9
			}
		}
		expected = {
			"sources": "Cache",
			"base": "NZD",
			"rates": {
				"AUD": 0.9
			}
		}
		output = cache_handler.formatCache(cache)
		self.assertDictEqual(output, expected)


if __name__ == "__main__":
	unittest.main()