
from rich.console import Console
import argparse
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from requests_handler import analyze_url_head
from flags_handler import parse_params, parse_auth

console = Console()

def main():
  #argparse config
  parser = argparse.ArgumentParser(
    prog="CiSec",
    description="OSINT & Vulnerabilities Scanner",
    epilog="Authorized use for educational purposes and permitted audits"
  )

  parser.add_argument("-u", "--url", help="URL target (ex: http://example.com)", required=True)
  parser.add_argument("--param", help='"key:value" | Parameters for the URL')
  parser.add_argument("--auth", help='"key:value" | Authorization to enter the URL')
  parser.add_argument("--insecure", action="store_true", help="Makes a insecure request, it does not stops in missing SSL/TLS")

  args = parser.parse_args()

  if args.url:
    #Initializes the request, checks if exists parameters and authorization, if exist it'll parse the value
    try:
      param_dict = None
      auth_dict = None
      verify_cert = True

      if args.param:
        parsed = parse_params(args.param)

      if args.auth:
        parsed = parse_auth(args.auth)
        if parsed:
          key, value = parsed
          auth_dict = {key: value}

      if args.insecure:
        verify_cert=False
        disable_warnings(InsecureRequestWarning)
        console.print("\n\t[bold gold1]WARNING:[/bold gold1] SSL verification disabled. Proceeding with insecure connection\n")


      scan = analyze_url_head(args.url, param_dict, auth_dict, verify_cert)

    except ValueError as e:
      print(f"[!] Error parsing arguments: {e}")
    except Exception as e:
      print(f"Unexpected error in main: {e}")

if __name__ == "__main__":
  main()