from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

def get_user_by_username(username, bearer_token):
    url = f'https://api.x.com/2/users/by/username/{username}'
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    username = input("Masukkan username yang ingin dicari: ")
    bearer_token = os.getenv('BEARER_TOKEN') # TODO : buat file '.env' dan isi dengan 'BEARER_TOKEN=***BEARER TOKEN ANDA***'

    output_dir = 'outputs'
    output_file = f'{username}.json'
    output_path = os.path.join(output_dir, output_file)

    try:
        user_data = get_user_by_username(username, bearer_token)
        print(user_data)

        os.makedirs(output_dir, exist_ok=True)

        with open(output_path, 'w') as json_file:
            json.dump(user_data, json_file, indent=4)

        print(f"User data telah disimpan di {output_path}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")
