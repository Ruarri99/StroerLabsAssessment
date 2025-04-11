class Metric():
	def __init__(self, api_name):
		self.api_name = api_name
		self.total_requests = 0
		self.total_valid_responses = 0

	def updateMetrics(self, response=True):
		self.total_requests += 1
		self.total_valid_responses += 1 if response else 0
		# Total Valid Responses only increases if the response contains the base and symbol currencies being queried, even if the response is 200

	def getName(self):
		return self.api_name

	def getMetrics(self):
		response = {
			"name": self.api_name,
			"metrics": {
				"total_requests": self.total_requests,
				"total_valid_responses": self.total_valid_responses
			}
		}
		return response


# Updates the metrics of the source apis, if the source is in the response's list of sources
def evaluateMetrics(response, api_metrics):
	for api in api_metrics:
		api.updateMetrics((True if api.getName() in response["sources"] else False))

	return api_metrics

# Formats and returns the metrics of all source apis
def requestMetrics(api_metrics):
	api_metric_reponses = [api.getMetrics() for api in api_metrics]
	total_queries = sum(api.get("metrics").get("total_requests") for api in api_metric_reponses)
	
	response = {
		"total_queries": total_queries,
		"apis": api_metric_reponses
	}

	return response