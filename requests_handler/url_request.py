
from rich import print

import requests as req
from .headers_comparison import check_headers
from .handle_url import check_url

def analyze_url(url, param=None, auth=None):
  try:
    checked_url = check_url(url)

    res = req.get(checked_url,
    timeout=5,
    params=param,
    auth=auth,
    allow_redirects=True)

    res.raise_for_status()

    sec_headers = check_headers(res.headers)

  except req.exceptions.ConnectionError as e:
    return f"[bold red][!][/bold red] Connection error: {e.__context__.__cause__.__cause__}"
  except req.exceptions.Timeout as e:
    return f"[bold red][!][/bold red] Timeout: {e}"
  except req.exceptions.HTTPError as e:
    if e.response.status_code >= 500:
      return f"[bold red][!][/bold red] Server error {e.response.status_code}: Server problems"
    elif e.response.status_code >= 400:
      if e.response.status_code == 403:
        return f"[bold gold1][!][/bold gold1] Status {e.response.status_code}: Think about include authorization"
      else:
        return f"[bold red][!][/bold red] Server did not respond: {e.response.status_code}"
    else:
      return f"[bold red][!][/bold red] HTTP/Protocol error: {e}"
  except req.exceptions.RequestException as e:
    return f"[bold red][!][/bold red] Unexpected error: {e}"
  else:
    return sec_headers