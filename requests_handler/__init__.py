
# request_handler/__init__.py

from .handle_url import check_url, print_headers
from .headers_comparison import check_headers
from .url_request import analyze_url

__all__ : ['check_url', 'check_headers', 'request']