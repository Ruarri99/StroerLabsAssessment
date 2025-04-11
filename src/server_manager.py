import json
from src import rates_manager
from src import metric_handler
from src import cache_handler
from http.server import BaseHTTPRequestHandler, HTTPServer


# Creates a handler for the server that passes in the api_metrics and api_cache as references
def makeHandler(api_metrics_classes=[], api_cache={}):
	class RequestHandler(BaseHTTPRequestHandler):
		def sendJSON(self, response, status_code=200):
			self.send_response(status_code)
			self.send_header("Content-type", "application/json")
			self.end_headers()
			self.wfile.write(json.dumps(response, indent=2).encode())


		def do_GET(self):
			if self.path.startswith("/metrics"):
				response = metric_handler.requestMetrics(api_metrics_classes)
				self.sendJSON(response)

			# Makes use of .split to get the variables from the URL - More error checking required
			elif self.path.startswith("/exchangeRates/"):
				try:
					endpoint = self.path.split("/")
					endpoint_params = endpoint[-1].split("?")
					base = endpoint_params[0]
					symbols = endpoint_params[1].split("symbols=")[1].split(",")

					inCache = cache_handler.checkCache(api_cache, base, symbols)

					if (inCache):
						rates = inCache
					else:
						rates = rates_manager.requestRates(base, ([] if symbols == [''] else symbols))
						api_cache.setdefault(rates.get("base"), {}).update(rates.get("rates"))

					metric_handler.evaluateMetrics(rates, api_metrics_classes)

					response = rates
					self.sendJSON(response)

				except IndexError:
					response = {"message": "Invalid endpoint"}
					self.sendJSON(response, 404)

			else:
				response = {"message": "Invalid endpoint"}
				self.sendJSON(response, 404)

	return RequestHandler


def makeServer(handler_class):
	server_address = ('', 8000)
	httpd = HTTPServer(server_address, handler_class)
	print("Hosting http server on http://localhost:" + str(server_address[1]) + "/")
	print("Metrics - http://localhost:" + str(server_address[1]) + "/metrics")
	print("Exchange Rates - http://localhost:" + str(server_address[1]) + "/exchangeRates/{baseCur}?symbols={SYM1,SYM2...}")

	return httpd

def runServer(httpd):
	httpd.serve_forever()