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
            [undefined_vars.append(k) for k,v in kwargs.items() if (v == "default" or v == 0)]

            if len(undefined_vars) != 0:
                joined_list = ", ".join(undefined_vars)
                raise ValueError(f"Please define undefined Variable{'' if len(undefined_vars) <= 1 else 's'}: {joined_list}")

            return True

        except Exception as e:
            return {
                "result": str(e),
                "changed": False,
                "failed": True
            }
            
    # Customers
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
                    "changed": False,
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

    # Customers
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

    # Customers
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
                    "changed": False,
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

    # Customers
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

    # Not really used at the moment
    # def get_catalogs(self):
    #     try:
    #         response = requests.get(
    #             url = f"{self.BASE_URL}/catalogs",
    #             auth = self.auth
    #         )

    #         print(response.json())

    #     except Exception as e:
    #         print(e)
    #         return False

    # Accounts
    def get_accounts(self):
        try:
            response = requests.get(
                url = f"{self.BASE_URL}/accounts",
                auth = self.auth,
                timeout = 20
            )

            if response.status_code == 200:
                accounts = response.json()
                return {
                    "result": f"Found {len(accounts)} Accounts in Platform: {self.PLATFORM_NAME}",
                    "changed": False,
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
    # Accounts
    def describe_account(self, account:str="default") -> dict:
        try:
            vars_defined = self.check_vars_defined(account=account)
            if vars_defined != True:
                return vars_defined

            response = requests.get(
                url = f"{self.BASE_URL}/accounts/{account}",
                auth = self.auth,
                headers = self.header
            )

            if response.status_code == 200:
                return {
                    "result": response.json(),
                    "changed": False,
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

    # Fund
    def register_credit_card(
        self, 
        customer_id:str="default", 
        account:str="default", 
        label:str="default",
        ip_address:str="default",
        card_number:str="default",
        card_expiration:str="default",
        card_verification_number:str="default",
        billing_first_name:str="default",
        billing_last_name:str="default",
        billing_address_line1:str="default",
        billing_city:str="default",
        billing_state:str="default",
        billing_postal:str="default",
        billing_country:str="default",
        billing_email:str="default",
        contact_full_name:str="",
        contact_email:str=""
    ) -> dict:
        try:
            vars_defined = self.check_vars_defined(
            customer_id=customer_id, 
            account=account, 
            label=label,
            ip_address=ip_address,
            card_number=card_number,
            card_expiration=card_expiration,
            card_verification_number=card_verification_number,
            billing_first_name=billing_first_name,
            billing_last_name=billing_last_name,
            billing_address_line1=billing_address_line1,
            billing_city=billing_city,
            billing_state=billing_state,
            billing_postal=billing_postal,
            billing_country=billing_country,
            billing_email=billing_email,
            contact_full_name=contact_full_name,
            contact_email=contact_email
            )
            if vars_defined != True:
                return vars_defined

            # for sandbox , switch to card number for ease of use
            if card_number == "visa":
                card_number = "4111111111111111"
            elif card_number == "mastercard":
                card_number = "5555555555554444"
            elif card_number == "discover":
                card_number = "6011111111111117"
            elif card_number == "american_express":
                card_number = "378282246310005"
            else:
                return {
                    "result": "Unrecognized card_number value. Must be one of visa, mastercard, discover, american_express",
                    "changed": False,
                    "failed": True
                }

            response = requests.post(
                url = f"{self.BASE_URL}/creditCards",
                auth = self.auth,
                headers = self.header,
                json = {
                    "accountIdentifier": account,
                    "billingAddress": {
                        "addressLine1": billing_address_line1,
                        "addressLine2": "",
                        "city": billing_city,
                        "country": billing_country,
                        "emailAddress": billing_email,
                        "firstName": billing_first_name,
                        "lastName": billing_last_name,
                        "postalCode": billing_postal,
                        "state": billing_state
                    },
                    "contactInformation": [
                        {
                        "emailAddress": contact_email,
                        "fullName": contact_full_name
                        }
                    ],
                    "creditCard": {
                        "expiration": card_expiration,
                        "number": card_number,
                        "verificationNumber": card_verification_number
                    },
                    "customerIdentifier": customer_id,
                    "ipAddress": ip_address,
                    "label": label
                }
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
            print(e)
            return {
                "result": str(e),
                "changed": False,
                "failed": True
            }

    # Fund
    def fund_account(self, customer_id:str="default", account:str="default", credit_card_token:str="default", amount:int=0) -> dict:
        try:
            vars_defined = self.check_vars_defined(account=account)
            if vars_defined != True:
                return vars_defined

            # for sandbox , switch to card number for ease of use
            if credit_card_token == "visa":
                credit_card_token = "4111111111111111"
            elif credit_card_token == "mastercard":
                credit_card_token = "5555555555554444"
            elif credit_card_token == "discover":
                credit_card_token = "6011111111111117"
            elif credit_card_token == "american_express":
                credit_card_token = "378282246310005"
            else:
                return {
                    "result": "Unrecognized credit_card_token value. Must be one of visa, mastercard, discover, american_express",
                    "changed": False,
                    "failed": True
                }

            print(credit_card_token)

            response = requests.post(
                url = f"{self.BASE_URL}/creditCardDeposits",
                auth = self.auth,
                headers = self.header,
                json = {
                    "customerIdentifier": customer_id,
                    "accountIdentifier": account,
                    "creditCardToken": credit_card_token,
                    "amount": amount
                }
            )

            print(response.json())

            if response.status_code == 200:
                return {
                    "result": response.json(),
                    "changed": False,
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



def main():
    f1 = Tango()
    # f1.get_customers()
    # f1.create_customer()
    # f1.describe_customer(customer_id="tester1")
    # f1.create_account(customer_id="tester1", account="another_account", email="tester5.account.email@yahoo.com")
    # f1.get_catalogs()
    f1.register_credit_card(
        customer_id="tester1", 
        account="tester7account", 
        label="tester1_label",
        ip_address="206.251.215.152",
        card_number="visa",
        card_expiration="2025-12",
        card_verification_number="123",
        billing_first_name="first",
        billing_last_name="last",
        billing_address_line1="address",
        billing_city="city",
        billing_state="tennessee",
        billing_postal="37167",
        billing_country="us",
        billing_email="bob@yahoo.com",
        contact_full_name="contact_full_name",
        contact_email="bobs_friend@yahoo.com"
    )
    # f1.fund_account(customer_id="tester1", account="tester7account", credit_card_token="visa", amount=100)

if __name__ == "__main__":
    main()