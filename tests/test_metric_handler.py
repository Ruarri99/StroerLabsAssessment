import unittest
from src import metric_handler

class TestMain(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def test_requestMetrics(self):
		cache = {
			"sources": "Cache",
			"base": "NZD",
			"rates": {
				"AUD": 0.9
			}
		}
		expected = {
			"name": "Cache",
			"metrics": {
				"total_requests": 1,
				"total_valid_responses": 1
			}
		}
		cache_metrics_class = metric_handler.Metric("Cache")
		api_metrics_classes = [cache_metrics_class]
		metric_handler.evaluateMetrics(cache, api_metrics_classes)
		output = api_metrics_classes[0].getMetrics()

		self.assertDictEqual(expected, output)


	def test_evaluateMetrics(self):
		cache = {
			"sources": "Cache",
			"base": "NZD",
			"rates": {
				"AUD": 0.9
			}
		}
		expected = {
			"total_queries": 1,
			"apis": [
				{
					"name": "Cache",
					"metrics": {
							"total_requests": 1,
							"total_valid_responses": 1
						}
				}
			]
		}
		cache_metrics_class = metric_handler.Metric("Cache")
		api_metrics_classes = [cache_metrics_class]

		metric_handler.evaluateMetrics(cache, api_metrics_classes)
		output = metric_handler.requestMetrics(api_metrics_classes)

		self.assertDictEqual(expected, output)


if __name__ == "__main__":
	unittest.main()