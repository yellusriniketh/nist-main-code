import requests
from bs4 import BeautifulSoup

base_url = "https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7782447&Type=IsoBar&Digits=5&P={}&THigh={}&TLow={}&TInc=1&RefState=DEF&TUnit=K&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=Pa*s&STUnit=N%2Fm"

pressure_value = 200  # Set your desired pressure value here
combined_content = ""

for t_low in range(60, 1200, 600):
    t_high = min(t_low + 599, 1200)
    url = base_url.format(pressure_value, t_high, t_low)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        html_content = soup.prettify()

        if t_low == 60:
            combined_content += html_content  # Include the whole HTML for the first chunk
        else:
            # Remove the first line (header) for subsequent chunks
            lines = html_content.splitlines()
            if lines:  # Check if the content is not empty
                combined_content += "\n".join(lines[1:]) #Join all lines except the first one.
    else:
        print(f"Failed to retrieve webpage for P={pressure_value}, TLow={t_low}, THigh={t_high}. Status code: {response.status_code}")

filename = f"oxygen_{pressure_value}.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(combined_content)
print(f"Webpage content saved to '{filename}'.")