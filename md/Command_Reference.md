# Command Reference

Examples of the two custom code-block languages the portal ships with.

## `prompt` blocks

Terminal sessions with prompt highlighting:

```prompt
user@kali:~$ nmap -sV 10.10.10.5   # quick scan
22/tcp   open  ssh
80/tcp   open  http
PS C:\Users\bud> Get-Process -Name explorer
```

## `csv` blocks

```csv
name,port,service
ssh,22,OpenSSH
http,80,nginx
```

## PowerShell

```powershell
Get-ADUser -Filter * | Select-Object Name, Enabled
```
