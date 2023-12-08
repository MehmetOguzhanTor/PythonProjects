import smtplib
import schedule
import requests
from bs4 import BeautifulSoup

def create_URL(city):
    url = "https://www.google.com/search?q=" + "weather condition" + city 
    html = requests.get(url).content 
    return html

def format_data(html):
    soup = BeautifulSoup(html, 
                     'html.parser') 
    temperature = soup.find( 
  'div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text 
    time_sky = soup.find( 
  'div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 
  
    # formatting data 
    sky = time_sky.split('\n')[1]
    return sky 

def main():
    html =create_URL("Trabzon")
    sky = format_data(html)

    print(sky)
    if sky == "Hafif sağanak yağmur" or sky == "Yağmurlu ve Karlı" or sky == "Sağanak Yağışlı" or sky == "Ūok bulutlu" or sky == "Çok bulutlu":
        print("Take an Umbrella")
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

if __name__ == "__main__":
    main()