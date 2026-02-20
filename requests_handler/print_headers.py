# Python modules
import re
from rich.console import Console
from rich.table import Table
from rich import box
# External modules
from .headers_comparison import check_headers

def print_headers(headers):

  checked_h = check_headers(headers)
  
  table = Table(title="Implemented Headers", box=box.ASCII)
  table.add_column("Name", justify="center", style="khaki1", no_wrap=True, header_style="bold khaki1")
  table.add_column("Directive", justify="center", style="deep_sky_blue1", no_wrap=True, header_style="bold deep_sky_blue1")
  table.add_column("Implemented", justify="center", style="bright_white", header_style="bold bright_white")
  for h in checked_h:
    if h['header_exists'] is False:
      table.add_row(h['header_name'], h['header_directive'], "[red]✘[/red]")
    else:
      table.add_row(h['header_name'], h['header_directive'], "[green]✔[/green]")

  console = Console()
  console.print(table)