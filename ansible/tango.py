import requests
import os
from requests.auth import HTTPBasicAuth
from icecream import ic



class Tango():
    def __init__(self):
        self.PLATFORM_NAME = os.environ["PLATFORM_NAME"]
        self.PLATFORM_KEY = os.environ["PLATFORM_KEY"]
        self.BASE_URL = "https://integration-www.tangocard.com/raas/v2"

    @property
    def auth(self):
        auth = HTTPBasicAuth(self.PLATFORM_NAME, self.PLATFORM_KEY)
        return auth

    @property
    def header(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        return headers

    def check_vars_defined(self, **kwargs):
        try:
            undefined_vars = []
            [undefined_vars.append(k) for k,v in kwargs.items() if v == "default"]

            if len(undefined_vars) != 0:
                joined_list = ", ".join(undefined_vars)
                raise ValueError(f"Please define undefined Var{'' if len(undefined_vars) <= 1 else 's'}: {joined_list}")

            return True

        except Exception as e:
            return {
                "result": str(e),
                "changed": False,
                "failed": True
            }
            

    def get_customers(self) -> dict:
        try:
            response = requests.get(
                url = f"{self.BASE_URL}/customers", 
                auth = self.auth,
                headers = self.header,
                timeout = 20
            )

            if response.status_code == 200:
                customers = response.json()
                return {
                    "result": f"Found {len(customers)} Customers in Platform: {self.PLATFORM_NAME}",
                    "changed": True,
                    "failed": False
                }
            
            else:
                return {
                    "result": f"Failed with Status Code {response.status_code}",
                    "changed": False,
                    "failed": True
                }
        except Exception as e:
            return {
                "result": str(e),
                "changed": False,
                "failed": True
            }

    def create_customer(self, customer_id:str="default", display_name:str="default" ) -> dict:
        try:
            vars_defined = self.check_vars_defined(customer_id=customer_id, display_name=display_name)
            if vars_defined != True:
                return vars_defined

            response = requests.post(
                url = f"{self.BASE_URL}/customers",
                json = {
                    "customerIdentifier": customer_id,
                    "displayName": display_name
                },
                auth = self.auth,
                headers = self.header,
                timeout = 10
            )

            if response.status_code == 200:
                return {
                    "result": response.json(),
                    "changed": True,
                    "failed": False
                }

            else:
                return {
                    "result": response.json().get("errors", {})[0].get("message", "Encountered Unknown Error"),
                    "changed": False,
                    "failed": True
                }
        
        except Exception as e:
            return {
                "result": str(e),
                "changed": False,
                "failed": True
            }

    def describe_customer(self, customer_id:str="default") -> dict:
        try:
            vars_defined = self.check_vars_defined(customer_id=customer_id)
            if vars_defined != True:
                return vars_defined

            response = requests.get(
                url = f"{self.BASE_URL}/customers/{customer_id}",
                auth = self.auth,
                headers = self.header
            )

            if response.status_code == 200:
                return {
                    "result": response.json(),
                    "changed": True,
                    "failed": False
                }

            else:
                return {
                    "result": response.json(),
                    "changed": False,
                    "failed": True
                }

        except Exception as e:
            print(e)
            return {
                "result": str(e),
                "changed": False,
                "failed": True
            }

    def create_account(self, customer_id:str="default", account:str="default", email:str="email") -> dict:
        try:
            response = requests.post(
                url = f"{self.BASE_URL}/customers/{customer_id}/accounts",
                json = {
                    "accountIdentifier": account,
                    "contactEmail": email,
                    "displayName": account
                },
                auth = self.auth,
                headers = self.header
            )

            if response.status_code == 201:
                return {
                    "result": response.json(),
                    "changed": True,
                    "failed": False
                }
            else:
                return {
                    "result": response.json(),
                    "changed": False,
                    "failed": True
                }

        except Exception as e:
            return {
                "result": str(e),
                "changed": False,
                "failed": True
            }

    def get_catalogs(self):
        try:
            response = requests.get(
                url = f"{self.BASE_URL}/catalogs",
                auth = self.auth
                # removed headers
            )

            # print(response.json("results": response))

        except Exception as e:
            print(e)
            return False



def main():
    f1 = Tango()
    # f1.get_customers()
    # f1.create_customer()
    # f1.describe_customer(customer_id="tester1")
    f1.create_account(customer_id="tester1", account="another_account", email="tester5.account.email@yahoo.com")
    # f1.get_catalogs()

if __name__ == "__main__":
    main()