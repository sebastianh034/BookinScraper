from bs4 import BeautifulSoup
import requests

bookings_page = requests.get("https://news.washeriff.net/divisions/bookings/")
soup = BeautifulSoup(bookings_page.text, "html.parser")
names = soup.select("div.name b")
charge = soup.find_all("div", attrs={'class': 'charge'})

for name , charge in zip(names, charge):
    print(name.text  + "\nCharges: " + charge.text)

