"""
"""
import os
from dotenv import load_dotenv
import requests

load_dotenv() #loads variables from the .env file into the environment
API_KEY = os.getenv('API_KEY') # os.getenv() to access the environment variables loaded from the .env file


def fetch_data(animal_name):
    """ Receives an 'animal name' from the user as an argument.
        Gets the animal information from the API by request GET.
        If the response is 'OK' returns the animal infos as json data, if not, prints an error in the terminal """
    API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(API_URL, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        json_data = response.json()
        return json_data
    else:
        print("Error:", response.status_code, response.text)


def main():
    pass
    
    
if __name__ == '__main__':
    main()
