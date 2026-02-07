
# Security Headers

SEC_HEADERS = {
    "Strict-Transport-Security": "HTTP Strict Transport Security (HSTS)",
    "X-XSS-Protection": "X-XSS-Protection",
    "X-Content-Type-Options": "X-Content-Type-Options",
    "X-Frame-Options": "X-Frame-Options",
    "Content-Security-Policy": "Content Security Policy (CSP)",
    "Public-Key-Pins": "HTTP Public-Key-Pins (HPKP)",
    "X-Permitted-Cross-Domain-Policies": "X-Permitted-Cross-Domain-Policies",
    "Referrer-Policy": "Referrer-Policy",
    "Expect-CT": "Expect-CT",
    "Permissions-Policy": "Permissions-Policy"
}

def check_headers(headers):
  
  h_list = list()

  for name, directive in SEC_HEADERS.items():
    if name in headers:
      h_list.append({
        "header_name": name,
        "header_directive": directive,
        "header_exists": True
      })

    else:
      h_list.append({
        "header_name": name,
        "header_directive": directive,
        "header_exists": False
      })


  return h_list