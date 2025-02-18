from bs4 import BeautifulSoup
import requests
from datetime import date

Arrests = 0
today = date.today()

Look_out = {'HERNANDEZ, JORGE','MARTINEZ, SONYA'}


bookings_page = requests.get("https://news.washeriff.net/divisions/bookings/")
soup = BeautifulSoup(bookings_page.text, "html.parser")

names = soup.select("div.name b")
charges = soup.find_all("div", attrs={'class': 'charge'})

for name, charge in zip(names, charges):
    name_text = name.text.strip().upper()
    Arrests += 1
    print("Name: "+ name.text + "\n" + "\nCharges: "f'{charge.text}' )
    
    if name_text in Look_out:
        print(f"🚨 ALERT: {name_text} Found! 🚨")
    
print("Number of Arrests for " f'{today}' ":"+ f' {Arrests}' + " total")

