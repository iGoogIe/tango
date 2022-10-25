# Tango POC

### Tango Ansible Project

This was initially written to learn Tango’s RaaS API. It provides a way to interact with Tango’s Sandbox API via Ansible (leveraging Python Action Plugins)

### Tango Documentation

- [Tango’s RaaS Documentation and Best Practices](https://developers.tangocard.com/docs/getting-started)
- [Tango Test Console](https://integration-www.tangocard.com/raas_api_console/v2/)

## Pre-Reqs

Setup the following Environment Variables

1. Via command line
    
    ```
    export PLATFORM_NAME = <TANGO_PLATFORM_NAME>
    export PLATFORM_KEY = <TANGO_PLATFORM_KEY>
    ```
    
2. Via .bashrc
    
    ```
    echo -e '\nexport PLATFORM_NAME=<TANGO_PLATFORM_NAME>' >> ~/.bashrc
    echo -e '\nexport PLATFORM_KEY=<TANGO_PLATFORM_KEY>' >> ~/.bashrc
    source ~/.bashrc
    ```
    

Setup a Virtual Environment and activate it

```
python3 -m venv .venv
source .venv/bin/activate
```

Install requirements.txt in the virtual environment (python 3+)

```
pip install -r tango_role/requirements.txt
```

## Use tango_role

| Task Description | Tag | Var(s) Required |
| --- | --- | --- |
| Get Output of Total Customers | get_customers | N/A |
| Create a Customer | create_customer | customer_id | display_name |
| Describe a Customer | describe_customer | customer_id |
| Create an Account (under a Customer) | create_account | customer_id | account | email |
| Get Output of Total Accounts | get_accounts | N/A |
| Describe an Account | describe_account | account |
| Register a Credit Card to a Customer/Account | register_credit_card | see tango_role/vars/main.yml |


### Run the Ansible Playbook with tags targeting what action(s) you want to take.

```
ansible-playbook runner.yml --tags "get_customers,create_customer”
```
- Note, the tags and task descriptions are defined in the table above

### Variables can be defined in tango/tango_role/vars/main.yml

- These variables are consumed by the ansible tasks that are ran
- In the table above, the variables necessary are defined in the Vars Column

### Variables can (optionally) be defined via command line as extra vars

```
ansible-playbook runner.yml -e "customer_id=random_customer_id" --tags describe_customer
```

- When passed in via command line , these take the highest precedence and override ALL other variables
    - See [Ansible Variable Precedence Documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#understanding-variable-precedence)