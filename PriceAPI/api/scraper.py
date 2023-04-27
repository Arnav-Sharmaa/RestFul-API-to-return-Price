import requests
from bs4 import BeautifulSoup

url="https://www.metal.com/Lithium-ion-Battery/202303240001"

def get_latest_price():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    name=soup.find("h1", class_="name___22hXH")
    price_element = soup.find("span", class_="priceDown___2TbRQ")
    element_name=name.text
    latest_price = price_element.text
    return [element_name,latest_price]
