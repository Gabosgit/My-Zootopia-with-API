"""
"""
import requests

API_KEY = '6bewdnhz1fGUW8ZTxDicPg==rQ3ByHHCt9MHRnCI'

def get_info_animal_by_name():
    name = input('Enter a name of an animal: ')
    API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(API_URL, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        json_data = response.json()
        return json_data
    else:
        print("Error:", response.status_code, response.text)


def main():
    animals_data = get_info_animal_by_name()
    print(animals_data)

if __name__ == '__main__':
    main()
