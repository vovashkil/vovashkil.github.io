import sys
import requests
from tabulate import tabulate

if (len(sys.argv) < 2):
    raise SystemExit("Usage: url_checker.py <url> <url> <url>")

results = []
for url in sys.argv[1:]:
    try:
        r = requests.get(url)
        results.append({ "URL" : url, "Status": r.status_code })
    except requests.RequestException as ex:
        results.append({ "URL" : url, "Status": type(ex).__name__ })

print(tabulate(results))

