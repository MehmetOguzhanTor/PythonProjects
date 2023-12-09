import smtplib
import schedule
import requests
from email import encoders
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

def create_URL(city):
  url = "https://www.google.com/search?q=" + "weather condition" + city 
  html = requests.get(url).content 
  return html

def format_data(html):
  soup = BeautifulSoup(html, 'html.parser') 
  temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text 
  time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 
  
  # formatting data 
  sky = time_sky.split('\n')[1]
  return temperature, sky 

def create_message(subject, body):
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = 'Your user name <Your Mail>'
    message['To'] = 'Your user name <Your mail>'
    return message

def send_email(subject, body):
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.starttls()
    smtp_object.login("Your Mail", "Your Password")

    msg = create_message(subject, body)
    encoded_msg = encoders.encode_base64(msg)

    smtp_object.sendmail('Your mail', 'Your mail', encoded_msg)

    smtp_object.quit()

def main():
  html = create_URL("Placeholder") #enter your city
  temperature, sky = format_data(html)

  print(sky)
  if sky == "Hafif sağanak yağmur" or sky == "Yağmurlu ve Karlı" or sky == "Sağanak Yağışlı" or sky == "Ūok bulutlu" or sky == "Çok bulutlu" or sky == "Ãok bulutlu":
    print("Take an Umbrella")

    send_email("Umbrella Reminder", f"Take an umbrella before leaving the house. Weather condition for today is {sky} and temperature is {temperature} in your city.")

    print("Email Sent!")


if __name__ == "__main__":
  main()
