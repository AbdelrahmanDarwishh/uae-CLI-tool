#UAE CLI Tool: Weather and Prayer Times

A simple command-line Python application that fetches real-time **weather data** and **Islamic prayer times** for cities in the **United Arab Emirates** using public APIs.

---

#Features

- Get real-time weather info: temperature, condition, humidity, wind speed
- Get today's prayer times: Fajr, Dhuhr, Asr, Maghrib, Isha
- Pretty terminal output using the `rich` library
- Works from the command line with city input
- Supports metric and imperial temperature units

---

#Installing the Dependancies: Run the following command
pip install -r requirements.txt

#Setting up your API key: Open weather.py and replace API_KEY with your actual key from https://openweathermap.org/

#Usage: Run the following (You can replace city and unit with any other values instead of Dubai and imperial)
python main.py --city Dubai --unit imperial

#Sample Output:
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Info        ┃ Value      ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Temperature │ 37 °C      │
│ Condition   │ Clear Sky  │
│ Humidity    │ 44%        │
│ Wind Speed  │ 5.1 m/s    │
│ Fajr        │ 04:13      │
│ Dhuhr       │ 12:21      │
│ Asr         │ 15:47      │
│ Maghrib     │ 18:56      │
│ Isha        │ 20:23      │
└─────────────┴────────────┘

#APIs Used:
OpenWeatherMap API
Aladhan Prayer Times API
