import requests

def get_cves():
    url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    response = requests.get(url)
    return response.json()

print("CVE Fetcher is working!")