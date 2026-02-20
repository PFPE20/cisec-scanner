#!/usr/bin/env python3

import os, sys

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) # This path
VENV_PKG = os.path.join(
  SCRIPT_DIRECTORY,
  'venv', 'lib',
  f'python{sys.version_info.major}.{sys.version_info.minor}',
  'site-packages'
)

if os.path.exists(VENV_PKG):
  sys.path.insert(0, VENV_PKG)


# Python modules
from rich.console import Console
import argparse
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
# External modules
import requests_handler as rh
import params_handler as ph
import fuzz_arch


console = Console()
err_cons = Console(stderr=True)

def main():
  #argparse config
  parser = argparse.ArgumentParser(
    prog='CiSec',
    description='OSINT & Vulnerabilities Scanner',
    epilog='Authorized use for educational purposes and permitted audits'
  )
  # -u flag is always required
  parser.add_argument('-u', '--url', help='URL target (ex: http://example.com)', required=True)
  # Headers zone
  parser.add_argument('-H', '--head', help='Prints implemented|not headers', action='store_true')
  parser.add_argument('--param', help='"key:value" | Parameters for the URL')
  parser.add_argument('--auth', help='"key:value" | Authorization to enter the URL')
  parser.add_argument('--insecure', action='store_true', help='Makes a insecure request, it does not stops in missing SSL/TLS')
  # Arch zone
  parser.add_argument('-A', '--arch', help='Try to fuzz architecture', action='store_true')

  args = parser.parse_args()

  if args.url:
    #Initializes the request, checks if exists parameters and authorization, if exist it'll parse the value
    scan = False
    try:
      param_dict = None
      auth_dict = None
      verify_cert = True

      if args.param:
        parsed = ph.parse_params(args.param)

      if args.auth:
        parsed = ph.parse_auth(args.auth)
        if parsed:
          key, value = parsed
          auth_dict = {key: value}

      if args.insecure:
        verify_cert=False
        disable_warnings(InsecureRequestWarning)
        console.print('\n\t[bold gold1]WARNING:[/bold gold1] SSL verification disabled. Proceeding with insecure connection\n')

      scan = rh.analyze_url(args.url, param_dict, auth_dict, verify_cert)

      if args.head:
        rh.print_headers(scan.headers)

      if args.arch:
        fuzz_arch.get_favicon(scan)
        fuzz_arch.get_unique_headers(scan)

    except ValueError as e:
      err_cons.print(f'\n\t[bold red3][!][/bold red3] Error parsing arguments: [italic]{e}[/italic]\n')
    except Exception as e:
      err_cons.print(f'\n\t[bold red3][!][/bold red3] Unexpected error in main: [italic]{e}[/italic]\n')







if __name__ == '__main__':
  main()
  #print()