from src import server_manager
from src import metric_handler


fcr_metrics_class = metric_handler.Metric("Free Currency Rates API")
ffa_metrics_class = metric_handler.Metric("Frankfurter.app API")
cache_metrics_class = metric_handler.Metric("Cache")
api_metrics_classes = [fcr_metrics_class, ffa_metrics_class, cache_metrics_class]

api_cache = {}

def main():
	handler_class = server_manager.makeHandler(api_metrics_classes, api_cache)
	httpd = server_manager.makeServer(handler_class)
	server_manager.runServer(httpd)