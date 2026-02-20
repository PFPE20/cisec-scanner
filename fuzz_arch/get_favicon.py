# Internal modules
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import codecs
import mmh3
from rich.console import Console
# External modules
import requests_handler as rh
from .favicon_hashes import FAVICON_HASH

console = Console()

def get_favicon(res):
  _html = res.text
  _url = res.url

  soup = BeautifulSoup(_html, 'html.parser')
  icon_link = soup.find('link', rel=lambda x: x and 'icon' in x.lower())
  if icon_link:
    icon_url = icon_link.get('href')
    icon_location = urljoin(_url, icon_url)
    req = rh.analyze_url(icon_location)
    _data = req.content

    _block = codecs.encode(_data, 'base64')
    _hash = mmh3.hash(_block)

    for entpr, srvs in FAVICON_HASH.items():
      for _srv, fvi_hash in srvs.items():
        if _hash == fvi_hash:
          console.print(f'The service "[bold cyan1]{_srv}[/bold cyan1]" from [bold cyan1]{entpr}[/bold cyan1] is running the server.')
          break
      else:
        continue
      break
    
    else:
      console.print(f'\n\t[bold gold1][!][/bold gold1] The hash [italic cyan1]{_hash}[/italic cyan1] is from an unknown service.\n')
          
  else:
    console.print('\n\t[bold gold1][!][/bold gold1] Not found\n')