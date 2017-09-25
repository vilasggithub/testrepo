import requests
from pprint import pprint
import sys


def main():
    city = "Philadelphia"
    res = ""
    # Can have a web-page to accept city and state, and then display the temperature and the weather
    # Can map urls to the function in the views.py and route accordingly to the templates for the form and the results
    # But the simple code to consume an API is here
    try:
        res = requests.get(
        "http://api.wunderground.com/api/7c1c38b610841bda/conditions/q/PA/Philadelphia.json")
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)
    else:
        weather = res.json()        # Get the json data
        pprint(weather)
        #print("The weather for " + weather['current_observation']['display_location']['country'])
        #print("The weather for " + weather['current_observation']['display_location']['state'])
        #print("The weather for " + weather['current_observation']['display_location']['city'])
        print('===============================================')
        print("The current temperature in " + weather['current_observation']['display_location']['full']) + " is:"
        print("\t" + str(weather['current_observation']['temp_f'])) + " Fahrenheit "
        print("Weather Conditions:")
        print("\tWeather: " + str(weather['current_observation']['weather']))
        print("\tRelative Humidity: " + str(weather['current_observation']['relative_humidity']))

        print("===============================================")



if __name__ == "__main__":
    main()