
# flags parser: param_handler.py

import re

def check_url(url):
  url.strip()
  regex_protocol = r'^https?\:\/\/'
  if re.match(regex_protocol, url):
    return url
  else:
    return f'https://{url}'



def parse_params(param_value):
  if not param_value:
    return None
    
  try:
    key, value = param_value.split(":", 1)
    return (key.strip(), value.strip())

  except ValueError:
    return f'[!] Invalid format: "{param_value}". Please use: "key:value"'



def parse_auth(auth_string):
  if not auth_string:
    return None

  try:
    key, value = auth_string.split(":", 1)
    return (key.strip(), value.strip())
    
  except ValueError:
    return f'[!] Invalid format: "{auth_string}". Please use: "key:value"'