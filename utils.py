import requests

def get_access_token(server_url, realm_name, client_id, client_secret, username, password, grant_type):
    token_url = f"{server_url}/realms/{realm_name}/protocol/openid-connect/token"
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password,
        'grant_type': grant_type
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(token_url, data=payload, headers=headers)
    response.raise_for_status()
    token = response.json()
    return token['access_token']
