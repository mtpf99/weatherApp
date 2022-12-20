from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests


# get API URL
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

#call API key from file using configparser

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key'] ['key']

# create function to return city weather data

# temperature fahrenheit, wind speed, weather icon, weather, pressure, humidity

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        wind_speed = ['wind'] [0]
        weather = json['weather'][0]['main']
        icon = json['weather'][0]['icon']
        humidity = json['main'] ['humidity']
        pressure = json['main'] ['pressure']
        final = (city, country, temp_fahrenheit, wind_speed, weather, icon,  humidity, pressure)
        return final
    else:
        return None


# create a function for search button
def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_label['text'] = '{}, {}'.format(weather[0], weather[1])
        temperature_label['text'] = '{:.2f}°F'.format(weather[2])
        windSpd_label['text'] = '{} m/S'.format(weather[3])
        weather_label['text'] = weather[4]

        humidity_label['text'] = 'humidity is {} %'.format(weather[6])
        pressure_label['text'] = '{}hPa'.format(weather[7])
    else:
        messagebox.showerror('Error', 'What city is? {}'.format(city))

#create window
app = Tk()
app.title('Get your Local Weather: ')
app.geometry('700x350')

# create input variables
city_text = StringVar()
city_entry = Entry(app, textvariable = city_text)
city_entry.pack()

#create button to search the weather
search_button = Button(app, text = '---Enter Your City--- ', width = 25, command = search, bg = 'blue', fg = 'white')
search_button.pack()
# Create place holders for data you want to import
# where the weather is
location_label = Label(app, text = 'Location', font = ('bold',25) )
location_label.pack()
# temperature
temperature_label = Label(app, text = '')
temperature_label.pack()
# weather conditions
weather_label = Label(app, text = '')
weather_label.pack()
# windspeed
windSpd_label = Label(app, text = '')
windSpd_label.pack()
# pressure
pressure_label = Label(app, text = '')
pressure_label.pack()
#humidity
humidity_label = Label(app, text = '')
humidity_label.pack()



#run the main loop
app.mainloop()


