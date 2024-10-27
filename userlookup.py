from dotenv import load_dotenv
import os
import requests

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
    username = 'leodicaprio' # TODO : UBAH USERNAME
    bearer_token = os.getenv('BEARER_TOKEN')
    try:
        user_data = get_user_by_username(username, bearer_token)
        print(user_data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")
