
from rich import print
import argparse

from requests_handler import analyze_url, print_headers
from flags_handler import parse_params, parse_auth


def main():
  #argparse config
  parser = argparse.ArgumentParser(
    prog="CiSec",
    description="OSINT & Security Scanner",
    epilog="Authorized use for educational purposes and permitted audits"
  )

  parser.add_argument("-u", "--url", help="URL target (ex: http://example.com)", required=True)
  parser.add_argument("--param", help='"key:value" | Parameters for the URL')
  parser.add_argument("--auth", help='"key:value" | Authorization to enter the URL')

  args = parser.parse_args()

  if args.url:
    #Initializes the request, checks if exists parameters and authorization, if exist it'll parse the value
    try:
      param_dict = None
      auth_dict = None

      if args.param:
        parsed = parse_params(args.param)

      if args.auth:
        parsed = parse_auth(args.auth)
        if parsed:
          key, value = parsed
          auth_dict = {key: value}

      scan = analyze_url(args.url, param_dict, auth_dict)
      if isinstance(scan, str):
        print(scan)
      else:
        print_headers(scan)

    except ValueError as e:
      print(f"[!] Error parsing arguments: {e}")
    except Exception as e:
      print(f"Unexpected error in main: {e}")

if __name__ == "__main__":
  main()