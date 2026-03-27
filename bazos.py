import requests
from bs4 import BeautifulSoup

url = "https://nabytek.bazos.cz/stoly/?hledat=&rubriky=nabytek&hlokalita=&humkreis=30&cenaod=0&cenado=1000&Submit=Hledat&order=&crp=&kitx=ano"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

advertisements: list[BeautifulSoup] = soup.find_all("div", "inzeraty")

for i, ad in enumerate(advertisements):
    print(f"{i+1}. Advertisement title: {ad.find("h2", "nadpis").text.strip()}")

    print("Description:")
    print(ad.find("div", "popis").text.strip())

    print(f"Price: {ad.find("div", "inzeratycena").text}")
    print(f"Location: {ad.find("div", "inzeratylok").text}")

    print("\n")
