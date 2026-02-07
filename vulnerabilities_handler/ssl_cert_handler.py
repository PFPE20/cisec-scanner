
from rich.console import Console
from rich.panel import Panel


console = Console()

def ssl_cert_failed():

  message = (
    "[bold red]CRITICAL: TRUST ANCHOR BROKEN[/bold red]\n\n"
    "The identity of this server could not be verified.\nFor an attacker, this is not just a bug; it is an open invitation to orchestate a Man-in-The-Middle attack."
    '[italic]"If you can not trust the identity of the server, you can not trust the data it provides."[/italic]\n\n'
    "[bold gold1]Potential Exploitation:[/bold gold1]\n\n[bold]Active Interception:[/bold] Local attackers can hijack this session right now.\n\n[bold]Data Integrity:[/bold] Any payload or header you analyze from this point onward could be spoofed.\n\n"
    "[bold][italic cyan1]Action:[/bold] investigation halted for safety. Use [bold bright_white]--insecure[/bold bright_white] to proceed into the void[/italic cyan1]"
  )

  panel = Panel(
    message,
    title="[bold red]SSL CERTIFICATE VALIDATION FAILED[/bold red]",
    border_style="gold1",
    expand=True,
    padding=(1, 2)
  )

  console.print(panel)
  return