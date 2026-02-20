# Internal modules
from rich.console import Console
import requests as req
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException, SSLError
from .headers_comparison import check_headers
# External modules
from vulnerabilities_handler import ssl_cert_failed
from params_handler import check_url
from .req_headers import req_headers

console = Console()
err_console = Console(stderr=True)

'''
This function analyzes only headers and receive data from the flags if provided. When an exception is caught, it will print its corresponding message.
'''

def analyze_url(url, param=None, auth=None, verify_cert=True):

  try:
    checked_url = check_url(url)

    res = req.get(checked_url,
    timeout=5,
    headers=req_headers(),
    params=param,
    auth=auth,
    verify=verify_cert,
    allow_redirects=True)

    res.raise_for_status()

    return res

  except SSLError:
    ssl_cert_failed()
    return
  except ConnectionError as e:
    err_console.print(f"\n\t[bold red][!][/bold red] Connection error: {e.__context__.__cause__}\n")
    return
  except Timeout as e:
    err_console.print(f"\n\t[bold red][!][/bold red] Timeout: {e}\n")
    return 
  except HTTPError as e:
    if e.response.status_code >= 500:
      err_console.print(f"\n\t[bold red][!][/bold red] Server error {e.response.status_code}: Server problems\n")
      return
    elif e.response.status_code >= 400:
      if e.response.status_code == 403:
        err_console.print(f"\n\t[bold gold1][!][/bold gold1] Status {e.response.status_code}: Think about include authorization\n")
        return
      else:
        err_console.print(f"\n\t[bold red][!][/bold red] Server did not respond: {e.response.status_code}\n")
        return
    else:
      err_console.print(f"\n\t[bold red][!][/bold red] HTTP/Protocol error: {e}\n")
      return
  except RequestException as e:
    err_console.print(f"\n\t[bold red][!][/bold red] Unexpected error: {e}\n")
    return
