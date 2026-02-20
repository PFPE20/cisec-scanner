# Internal modules
import random as rdm
from math import ceil

# UAs to requests
user_agents = [
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36', # Chrome Windows
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0', # Edge Windows
  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36', # Brave Linux
  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0' # Firefox Linux
]

'''
This function set the headers to the request module
'''

def req_headers():

  rand_num = (rdm.random() * len(user_agents)) - 1
  _ua = ceil(rand_num)

  headers = {
    'User-Agent': user_agents[_ua],
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1', # Do Not Track
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
  }

  return headers