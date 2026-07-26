# Networking Cheatsheet

A quick-reference guide, demonstrating a longer document with several
sections and nested lists.

## Subnetting quick reference

| CIDR | Mask            | Hosts |
| ---- | --------------- | ----- |
| /24  | 255.255.255.0   | 254   |
| /25  | 255.255.255.128 | 126   |
| /26  | 255.255.255.192 | 62    |
| /27  | 255.255.255.224 | 30    |
| /30  | 255.255.255.252 | 2     |

## Common ports

- 22 — SSH
- 25 — SMTP
- 53 — DNS
- 80 / 443 — HTTP / HTTPS
- 3389 — RDP

## Troubleshooting checklist

1. Check physical connectivity (link lights, cabling)
2. Confirm IP configuration
   - Correct subnet mask
   - Correct default gateway
3. Test name resolution
   ```bash
   nslookup example.com
   ```
4. Test reachability
   ```bash
   ping -c 4 8.8.8.8
   traceroute 8.8.8.8
   ```
5. Check firewall rules on both ends

## Useful `csv` snippet

```csv
device,role,ip
router-1,gateway,10.0.0.1
switch-1,access,10.0.0.2
```

> Tip: keep a running inventory of static assignments to avoid IP conflicts
> on the network.
