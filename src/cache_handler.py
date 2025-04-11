def checkCache(cache, base, symbols):
	inCache = {"rates": {}}
	if cache.get(base):
		inCache["base"] = base
		for sym in symbols:
			if cache.get(base).get(sym):
				inCache["rates"][sym] = cache.get(base).get(sym)
			else:
				return []
			
		return formatCache(inCache)
	
	else:
		return []
	
	
def formatCache(cache):
	response = {
		"sources": "Cache",
		"base": cache.get("base"),
		"rates": cache.get("rates")
	}

	return response