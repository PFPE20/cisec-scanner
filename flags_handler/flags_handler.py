
# flags parser: flags_handler.py

'''
Both functions transform provided data from the user in necessary data for the correct use of the request. Parameters for the request are dicts and authorization are tuples
'''
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