import os
from dotenv import load_dotenv
import requests
import telebot

try:
    load_dotenv()
except Exception as e:
    print(f"Error loading .env file: {e}")


BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def get_weather_data(api_key, city):
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['current']['temp_c']
            description = data['current']['condition']['text']
            return f"The current weather in {city} is {temperature}°C with {description}."
        else:
            return f"Failed to fetch weather data. Status code: {response.status_code}"
    except Exception as e:
        return f"Error fetching weather data: {e}"

# Example usage
api_key = 'x'
city = 'London'
weather_data = get_weather_data(api_key, city)
print(weather_data)



bot.infinity_polling()