import urllib.request
import json

# Sends out api calls and formats the response into a dict
def requestRates(base="nzd", symbols=[]):
	api_FCR_rates = freeCurrencyRates(base, symbols)
	api_FFA_rates = frankfurterApp(base, symbols)

	if api_FCR_rates and api_FFA_rates:
		combined_rates = combineRates(api_FCR_rates, api_FFA_rates)
		response = formatResponse(base, combined_rates)

	elif api_FCR_rates:
		response = formatResponse(base, api_FCR_rates, sources=["Free Currency Rates API"])

	else:
		response = formatResponse(base, api_FFA_rates, sources=["Frankfurter.app API"])
	
	return response


# API call for rates from Free Currency Rates API
def freeCurrencyRates(base="nzd", symbols=[]):
	base = base.lower()
	symbols = [symbol.lower() for symbol in symbols]
	url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/" + base + ".json"
	data = apiRequest(url)

	if symbols:
		data[base] = {k: v for k, v in data[base].items() if k in symbols}

	return data.get(base, {})


# API call for Frankfurter.app API
def frankfurterApp(base="nzd", symbols=[]):
	url = "https://api.frankfurter.dev/v1/latest?base=" + base + (("&symbols=" + ",".join(symbols)) if symbols else "")
	data = apiRequest(url)

	return data.get("rates", {})


# API call using urllib.request
def apiRequest(url):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
	}
	req = urllib.request.Request(url, headers=headers)

	try:
		with urllib.request.urlopen(req) as response:
			data = json.load(response)

	except urllib.request.HTTPError as err:
		if err.code != 404:
			raise

		else:
			data = {}

	return data


# Averages any matching rates from the two API responses, and creates one list of rates
def combineRates(api1_rates, api2_rates):
	combined_rates = {k.upper(): v for k, v in api1_rates.items()}

	for k, v in api2_rates.items():
		if k.upper() in combined_rates:
			combined_rates[k.upper()] = (combined_rates[k.upper()] + v) / 2
			
		else:
			combined_rates[k.upper()] = v

	return combined_rates


def formatResponse(base, rates, sources=["Free Currency Rates API", "Frankfurter.app API"]):
	response = {
		"sources": sources,
		"base": base.upper(),
		"rates": {k.upper(): v for k, v in rates.items()}
	}

	return response