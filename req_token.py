import requests

class InitializeToken:
    def __init__(self, client_id, client_secret):
        self.auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        self.data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }

        self.token = None

    def get_access_token(self):
        """Gets the access token."""

        response = requests.post(self.auth_url, headers=self.headers, data=self.data)

        if response.status_code == 200:
            self.token = response.json().get('access_token')
            print("Access Token:", self.token)

        else:
            print(f"Error: {response.status_code}")

        return self.token