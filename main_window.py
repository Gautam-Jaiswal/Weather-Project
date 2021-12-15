from tkinter import *
from tkinter import simpledialog
import requests
import datetime

api_key = 'Your API Key'
api_call = 'https://api.openweathermap.org/data/2.5/onecall'
my_lat = Your latitude
my_long = Your longitude
exclude = ['current', 'minutely', 'hourly']
parameters = {
    'lat': my_lat,
    'lon': my_long,
    'exclude': 'current,minutely,hourly',
    'units': 'metric',
    'appid': api_key
}
FONT = 'Roboto 20  italic'


class Main_Window:

    def __init__(self):
        self.window = Tk()
        self.window.title("Weather App")
        self.window.config(bg='white', padx=20, pady=20)

        self.day = simpledialog.askstring(title='Input Day',
                                          prompt='Enter "T" for "Today" and "TO" for "Tomorrow"').lower()
        if self.day == 'to':
            self.input_value = 1
        else:
            self.input_value = 0

        self.response = requests.get(api_call, params=parameters)
        self.response.raise_for_status()
        self.data = self.response.json()['daily'][self.input_value]

        self.sunrise_time = datetime.datetime.fromtimestamp(int(self.data['sunrise'])).time()
        self.sunset_time = datetime.datetime.fromtimestamp(int(self.data['sunset'])).time()
        self.moonrise = datetime.datetime.fromtimestamp(int(self.data['moonrise'])).time()

        self.min_temp = self.data['temp']['min']
        self.max_temp = self.data['temp']['max']

        self.wind_speed = self.data['wind_speed']

        self.weather_description = self.data['weather'][0]['description']
        self.weather_icon = str(self.data['weather'][0]['icon'])
        self.weather_icon = 'd' + self.weather_icon[:2]

        self.sunrise = PhotoImage(file='Icons/Sunrise.png')
        self.sunset = PhotoImage(file='Icons/Sunset.png')
        self.LowTemp = PhotoImage(file='Icons/LowTemp.png')
        self.HighTemp = PhotoImage(file='Icons/HighTemp.png')
        self.moon = PhotoImage(file='Icons/Moon.png')
        self.wind = PhotoImage(file='Icons/wind.png')

        self.Sunrise_Label = Label(master=self.window, image=self.sunrise)
        self.Sunrise_Label.grid(row=1, column=0, padx=20, pady=20)
        self.sunrise_time_label = Label(master=self.window, text='hello', font=FONT)
        self.sunrise_time_label.grid(row=2, column=0)

        self.Sunset_Label = Label(master=self.window, image=self.sunset)
        self.Sunset_Label.grid(row=1, column=1, padx=20, pady=20)
        self.sunset_time_label = Label(master=self.window, text='hello', font=FONT)
        self.sunset_time_label.grid(row=2, column=1)

        self.LowTemp_Label = Label(master=self.window, image=self.LowTemp)
        self.LowTemp_Label.grid(row=3, column=0, padx=20, pady=20)
        self.lowtemp_time_label = Label(master=self.window, text='hello', font=FONT)
        self.lowtemp_time_label.grid(row=4, column=0)

        self.HighTemp_Label = Label(master=self.window, image=self.HighTemp)
        self.HighTemp_Label.grid(row=3, column=1, padx=20, pady=20)
        self.hightemp_time_label = Label(master=self.window, text='hello', font=FONT)
        self.hightemp_time_label.grid(row=4, column=1)

        self.Moon_Label = Label(master=self.window, image=self.moon)
        self.Moon_Label.grid(row=5, column=0, padx=20, pady=20)
        self.moon_time_label = Label(master=self.window, text='hello', font=FONT)
        self.moon_time_label.grid(row=6, column=0)

        self.Wind_Label = Label(master=self.window, image=self.wind)
        self.Wind_Label.grid(row=5, column=1, padx=20, pady=20)
        self.wind_speed_label = Label(master=self.window, text='hello', font=FONT)
        self.wind_speed_label.grid(row=6, column=1)

        self.d01 = PhotoImage(file='WeatherIcons/01d@2x.png')
        self.d02 = PhotoImage(file='WeatherIcons/02d@2x.png')
        self.d03 = PhotoImage(file='WeatherIcons/03d@2x.png')
        self.d04 = PhotoImage(file='WeatherIcons/04d@2x.png')
        self.d09 = PhotoImage(file='WeatherIcons/09d@2x.png')
        self.d10 = PhotoImage(file='WeatherIcons/10d@2x.png')
        self.d11 = PhotoImage(file='WeatherIcons/11d@2x.png')
        self.d13 = PhotoImage(file='WeatherIcons/13d@2x.png')
        self.d50 = PhotoImage(file='WeatherIcons/50d@2x.png')

        self.weatherIcon = Label(master=self.window, image=self.d13)
        self.weatherIcon.grid(row=0, column=0)
        self.weatherText = Label(master=self.window, text='hello hj njk', font=FONT)
        self.weatherText.grid(row=0, column=0, columnspan=2)

        self.update_weather()

        self.window.mainloop()

    def update_weather(self):

        self.sunrise_time_label.config(text=self.sunrise_time)
        self.sunset_time_label.config(text=self.sunset_time)

        self.lowtemp_time_label.config(text=self.min_temp)
        self.hightemp_time_label.config(text=self.max_temp)

        self.wind_speed_label.config(text=self.wind_speed)
        self.moon_time_label.config(text=self.moonrise)

        self.weatherText.config(text=self.weather_description)
        weather_icon = str(self.weather_icon)
        if weather_icon == 'd01':
            self.weatherIcon.config(image=self.d01)
        elif weather_icon == 'd02':
            self.weatherIcon.config(image=self.d02)
        elif weather_icon == 'd03':
            self.weatherIcon.config(image=self.d03)
        elif weather_icon == 'd04':
            self.weatherIcon.config(image=self.d04)
        elif weather_icon == 'd09':
            self.weatherIcon.config(image=self.d09)
        elif weather_icon == 'd10':
            self.weatherIcon.config(image=self.d10)
        elif weather_icon == 'd11':
            self.weatherIcon.config(image=self.d11)
        elif weather_icon == 'd13':
            self.weatherIcon.config(image=self.d13)
        elif weather_icon == 'd50':
            self.weatherIcon.config(image=self.d50)