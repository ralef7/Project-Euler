#weather in all baseball towns:


#
# Washington, DC

import json
from urllib.request import urlopen


# 2. Display the city and weather information at each airport:
#
# ORD (Chicago): The temperature is 30.0 F (-1.1 C), and the wind is Northeast at 8.1mph.
# LAX (Los Angelese): The temperature is 65.0 F (18.3 C), and the wind is Variable at 4.6mph.
# etc.

# Here's a function to help you get started:

def get_airport_info(airport_code):
  # print(sport)
  url = "http://services.faa.gov/airport/status/" + airport_code + "?format=application/json"
  data = urlopen(url).read().decode()
  result = json.loads(data)
  return result

def get_weather(airport_code):
  sport = "hockey"
  get_airport_info(airport_code)


get_weather("ORD")


# TO DO: Write your code here.  Feel free to modify the code above, too.
#
# ORD (Chicago): The temperature is 30.0 F (-1.1 C), and the wind is Northeast at 8.1mph.
airport_codes = ['ORD', 'SFO', 'JFK', 'PHL', 'LAX', 'BOS', 'BWI', 'PHX', 'ATL', 'CLE', 'CVG', 'DTW', 'DEN',
                 'IAH', 'MCI', 'MIA', 'MKE', 'MSP', 'OAK', 'PIT', 'SEA', 'SAN', 'TPA', 'DFW', 'STL', 'DCA', 'BUF']


for airport_code in airport_codes:
  info = get_airport_info(airport_code)
  print(info['city'], info['weather']['temp'],
    info['weather']['wind'])

def csv_writer(data, path):
  with open(path, 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter = "")
    for line in data:
      writer.writerow(line)

if __name__ == "__main__":
  data = [['city, temperature, wind'.split(",")],
          get_aiport_info(airport_code)]

