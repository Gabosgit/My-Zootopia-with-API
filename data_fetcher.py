"""
"""
import os
from dotenv import load_dotenv
import requests

load_dotenv() #loads variables from the .env file into the environment

API_KEY = os.getenv('API_KEY') # os.getenv() to access the environment variables loaded from the .env file


def fetch_data(animal_name):
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


