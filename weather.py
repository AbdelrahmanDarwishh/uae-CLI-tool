import requests     #Make HTTP requests to web APIs in general

API_KEY = "YOUR_API_KEY"  #This tells us which API we want to access and 
                                                #authenticates your access to their service

def get_weather(city, unit="metric"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},AE&appid={API_KEY}&units={unit}"
    #How do we know this program works for which country?
        # --> The country code is specified as "AE" for the United Arab Emirates
    response = requests.get(url)    #Sends GET request to the API endpoint
    data = response.json()          #Transforming the response into JSON format (Dictionary Format)

    return {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"]
    }


# # CODE TESTING:
# if __name__ == "__main__":
#     result = get_weather("Dubai")
#     print(result)


