from tkinter import *

win = Tk()
canvas = Canvas(win, width=400, height=300, relief='raised')



canvas.pack()
# set up your labels label 1
lab1 = Label(win, text='Get your Daily Weather Report!')
lab1.config(font=('helvetica', 14))
canvas.create_window(200, 25, window=lab1)
#label 2
lab2 = Label(win, text='Enter your City:')
lab2.config(font=('helvetica', 10))
canvas.create_window(200, 100, window=lab2)
# create entry variable for your city
entry1 = Entry(win)
canvas.create_window(200, 140, window=entry1)

'''API_key = ""
weather_URL = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_key + "&q=" + str(a1)
city_WeatherData = requests.get(weather_URL).json()
print("Your forecast for today is: " + str(city_WeatherData))
display = Label(newwin, text="Your weather is currently: ")
display.pack()'''
