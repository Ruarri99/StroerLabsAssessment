import unittest
import threading
import json
import urllib.request
import src.server_manager

class TestMain(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.httpd = src.server_manager.makeServer(src.server_manager.makeHandler())
		cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
		cls.thread.start()

	@classmethod
	def tearDownClass(cls):
		cls.httpd.shutdown()
		cls.thread.join()

	def test_server_response(self):
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
		}
		req = urllib.request.Request("http://localhost:8000/metrics", headers=headers)

		with urllib.request.urlopen(req) as response:
			data = json.load(response)

		self.assertEqual(data["total_queries"], 0)


if __name__ == "__main__":
	unittest.main()