import requests
from urllib.parse import urlencode

# Define your credentials and parameters
CLIENT_ID = 'uhvGoDscmT5lj26D5R'
CLIENT_SECRET = 'F^2dL!N1Gl&#1YiD%w*sc^!fd69B4c4i'
REDIRECT_URI = 'http://127.0.0.1:8080/callback'
SCOPE = 'state'
CODE = 'code'
AUTHORIZATION_BASE_URL = 'https://dida365.com/oauth/authorize'
TOKEN_URL = 'https://dida365.com/oauth/token'

def get_authorization_url():
    """Generate the authorization URL."""
    authorization_url = f"{AUTHORIZATION_BASE_URL}?" + urlencode({
        'client_id': CLIENT_ID,
        'response_type': CODE,
        'redirect_uri': REDIRECT_URI,
        'scope': SCOPE
    })
    return authorization_url

def exchange_code_for_token(authorization_code):
    """Exchange the authorization code for an access token."""
    token_data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET  # Replace with your actual client secret
    }
    
    response = requests.post(TOKEN_URL, data=token_data)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Failed to obtain access token: {response.json()}")

def fetch_tasks(access_token):
    """Fetch tasks using the access token."""
    api_url = 'https://api.dida365.com/api/v2/task'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch tasks: {response.json()}")

def main():
    # Step 1: Get the authorization URL and prompt user to authorize
    print('Please go to this URL and authorize:', get_authorization_url())
    
    # Step 2: After user authorizes, capture the authorization code from the redirect
    authorization_code = input('Enter the authorization code you received: ')
    
    try:
        # Exchange the authorization code for an access token
        access_token = exchange_code_for_token(authorization_code)
        print('Access token:', access_token)

        # Step 3: Use the access token to fetch tasks
        tasks = fetch_tasks(access_token)
        print('Tasks:', tasks)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
