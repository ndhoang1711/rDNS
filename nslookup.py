
import os
import requests
import sys
import pandas as pd
from tabulate import tabulate

# ipinfo API token
API_TOKEN = '1c1c751ead9839'
ip = input("Enter IP to check DNS:")
pages = 1 
def query_ip(ip):
    url = f"https://ipinfo.io/domains/{ip}?token={API_TOKEN}"
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            response.raw.decode_content = True  # Ensure the content is decoded correctly
            json_response = response.json()
            return json_response
        else:
            print(f"Failed to retrieve data for {ip}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error querying IP {ip}: {e}")
    return None

result = query_ip(ip)
if result:
    domains_info = result.get('domains')
    print("Domain of IP " + str(ip)  + " is: " + str(domains_info[0]))