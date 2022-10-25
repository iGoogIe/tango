# Tango POC
Provides a way to interact with Tango’s Sandbox API via Ansible (leveraging Python Action Plugins)

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

## Running from the tango_role

- Available tasks
    - 
    
    | Task | Tag |
    | --- | --- |
    | get_customers.yml | get_customers |
    |  |  |

```
ansible-playbook runner.yml --tags "get_customers,create_customer”
```

Variables can be defined in tango/tango_role/vars/main.yml

- These variables are consumed by the ansible tasks that are ran

Variables can (optionally) be defined via command line as extra vars

```
ansible-playbook runner.yml -e "customer_id=random_customer_id"
```

- When passed in via command line , these override ALL other variables
    - See [Ansible Variable Precedence Documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#understanding-variable-precedence)

### Running outside of tango_role (this is more for local testing / seeing what’s in the roles)

```
cd tango/ansible
ansible-playbook main.yml
```