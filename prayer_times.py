import requests

def get_prayer_times(city):
    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=UAE&method=8"
    response = requests.get(url)
    data = response.json()

    return {
        "Fajr": data["data"]["timings"]["Fajr"],
        "Dhuhr": data["data"]["timings"]["Dhuhr"],
        "Asr": data["data"]["timings"]["Asr"],
        "Maghrib": data["data"]["timings"]["Maghrib"],
        "Isha": data["data"]["timings"]["Isha"],
    }


