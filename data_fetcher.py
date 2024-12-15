"""
"""
import requests
API_KEY = '6bewdnhz1fGUW8ZTxDicPg==rQ3ByHHCt9MHRnCI'

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


