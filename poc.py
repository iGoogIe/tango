import requests
import os
from requests.auth import HTTPBasicAuth
from icecream import ic



class Tango():
    def __init__(self):
        self.PLATFORM_NAME = os.environ["PLATFORM_NAME"]
        self.PLATFORM_KEY = os.environ["PLATFORM_KEY"]
        self.BASE_URL = "https://integration-www.tangocard.com/raas/v2"

        print(self.PLATFORM_KEY, self.PLATFORM_NAME)

    @property
    def auth(self):
        auth = HTTPBasicAuth(self.PLATFORM_NAME, self.PLATFORM_KEY)
        return auth

    @property
    def basic_headers(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        return headers

    def get_customers(self):
        try:
            response = requests.get(
                url=f"{self.BASE_URL}/customers", 
                auth=(
                    self.PLATFORM_NAME, 
                    self.PLATFORM_KEY
                )
            )

            if response.status_code == 200:
                customers = response.json()
                print(f"Found {len(customers)} Customers")
            
            else:
                print(f"Got a bad response {response.status_code}")
        except Exception as e:
            print(e)
            return False

    def create_customer(self):
        try:
            response = requests.post(
                url = f"{self.BASE_URL}/customers",
                json = {
                    "customerIdentifier": "tester1",
                    "displayName": "tester1"
                },
                headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                auth = self.auth
            )

            print(response.text)
        
        except Exception as e:
            print(e)
            return False

    def describe_customer(self, cust_id):
        try:
            response = requests.get(
                url = f"{self.BASE_URL}/customers/{cust_id}",
                auth = self.auth
            )

            print(response.text)

        except Exception as e:
            print(e)
            return False

    def create_account(self, cust_id, account, email):
        try:
            response = requests.post(
                url = f"{self.BASE_URL}/customers/{cust_id}/accounts",
                json = {
                    "accountIdentifier": account,
                    "contactEmail": email,
                    "displayName": account
                },
                headers = self.basic_headers,
                auth = self.auth
            )

            # TODO: return account number if expected response

            print(response.text)

        except Exception as e:
            print(e)
            return False



def main():
    f1 = Tango()
    # f1.get_customers()
    f1.create_customer()
    f1.describe_customer(cust_id="tester1")
    f1.create_account(cust_id="tester1", account="tester1account", email="tester.account.email@yahoo.com")

if __name__ == "__main__":
    main()