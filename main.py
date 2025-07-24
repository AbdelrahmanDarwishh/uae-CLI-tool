#Part 1: Making the parser object, and adding an argument for the city name

import argparse

parser = argparse.ArgumentParser(description="UAE CLI Tool")
parser.add_argument("--city", required=True, help="Enter the UAE city name")
args = parser.parse_args()



#Part 2: Formatting the output using Rich (Colors, Tables, etc.)
from weather import get_weather
from prayer_times import get_prayer_times
from rich.console import Console
from rich.table import Table

# Replace with your actual API call
weather = get_weather(args.city)
prayer_times = get_prayer_times(args.city)

console = Console()
table = Table(title=f"{args.city.title()} - Weather & Prayer Times")

table.add_column("Info", style="cyan")
table.add_column("Value", style="magenta")

table.add_row("Temperature", f"{weather['temp']} °C")
table.add_row("Condition", weather["description"].title())
table.add_row("Humidity", f"{weather['humidity']}%")
table.add_row("Wind Speed", f"{weather['wind_speed']} m/s")

table.add_section()
for prayer, time in prayer_times.items():
    table.add_row(prayer, time)

console.print(table)
