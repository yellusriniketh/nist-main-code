import requests
from bs4 import BeautifulSoup
import os

def extract_data(p):
    base_url = "https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7727379&Type=IsoBar&Digits=5&P={}&THigh=1200&TLow=77&TInc=1&RefState=DEF&TUnit=K&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=Pa*s&STUnit=N%2Fm"
    url = base_url.format(p)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        filename = f"dodecane_{p}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(soup.prettify())
        print(f"Webpage content saved to '{filename}'.")
    else:
        print(f"Failed to retrieve the webpage for P={p}. Status code: {response.status_code}")

# Example usage
pressure_value =350  # Replace with the desired pressure value
extract_data(pressure_value)