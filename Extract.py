import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

base_url = "https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7782447&Type=IsoBar&Digits=5&P={}&THigh=2000&TLow=60&TInc=1&RefState=DEF&TUnit=K&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=Pa*s&STUnit=N%2Fm"
# Create a list to hold the contents of all txt files
for p in range(60, 161):
    url = base_url.format(p)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        filename = f"webpage_content_{p}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(soup.prettify())
        print(f"Webpage content saved to '{filename}'.")
    else:
        print(f"Failed to retrieve the webpage for P={p}. Status code: {response.status_code}")