# External modules
import requests_handler as rh

def get_unique_headers(_h):
  res_h = dict(_h.headers)
  
  for h_key, h_value in res_h.items():
    print(f'{h_key}: {h_value}')
