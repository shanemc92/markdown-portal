# Welcome to the Portal

This is a demo guide showing off the renderer's features. Drop your own
`.md` files into `md/` and re-run `generate_index.py`.

## Text formatting

Standard GFM works out of the box: **bold**, *italics*, `inline code`,
and [links](https://github.com).

- Bullet one
- Bullet two
  - Nested item
- [x] Completed task
- [ ] Open task

## Tables

| Port | Service | Notes           |
| ---- | ------- | --------------- |
| 22   | SSH     | Key auth only   |
| 80   | HTTP    | Redirects to 443|
| 443  | HTTPS   | TLS 1.2+        |

## Code blocks

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

```bash
sudo apt update && sudo apt upgrade -y
```

## Blockquote

> Everything renders client-side — no build step, no server required
> beyond a static file host.

See [Command Reference](Command_Reference.md) for the custom `csv` and
`prompt` code block styles.
