import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

base_url = "https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7782447&Type=IsoBar&Digits=5&P={}&THigh=660&TLow=60&TInc=1&RefState=DEF&TUnit=K&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=Pa*s&STUnit=N%2Fm"

# Create a list to hold the contents of all txt files
data = []

for p in range(1, 10):
    url = base_url.format(p)
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        filename = f"oxygen_{p}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(soup.prettify())
        print(f"Webpage content saved to '{filename}'.")

        # Extract data from the soup object and append to the data list
        # Log the structure of the HTML content for debugging
        print(f"HTML content for P={p}:")
        print(soup.prettify()[:1000])  # Print the first 1000 characters of the HTML content

        table = soup.find('table')
        if table:
            df = pd.read_html(str(table))[0]
            df['Pressure'] = p
            data.append(df)
        else:
            print(f"No table found on the webpage for P={p}.")

    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage for P={p}. Error: {e}")

# Save the collected data to a CSV file
if data:
    result_df = pd.concat(data, ignore_index=True)
    result_df.to_csv("oxygen_data.csv", index=False)
    print("Data saved to 'oxygen_data.csv'.")
else:
    print("No data collected.")