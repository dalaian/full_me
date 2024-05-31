import os
import yaml
 
 
with open('./utils/config_data.yaml', 'r') as file:
    config = yaml.safe_load(file)
 
 
# Accessing configuration values
url = config['url']
url_logged = config['url_logged']

user_name = config['user']['name']
user_pass = config['user']['pass']

# Email
email_from = config['email']['from']
email_from_pass = os.environ.get('email_password', config['email']['pass'])
email_to = os.environ.get('EMAIL', config['email']['to'])

# Configuration
CI = os.environ.get('CI', config['CI'])