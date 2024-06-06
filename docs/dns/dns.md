###### back to repo's main [README.md](../../README.md)
# DNS misc
### Clear cache pdns-recursor + dnsdist
#### pdns-recursor
```
# rec_control wipe-cache example.domain.com
wiped 1 records, 1 negative records, 2 packets
```
#### dnsdist
```
# dnsdist -c
> getPool(""):getCache():expungeByName(newDNSName("example.domain.com"), DNSQType.A)
Expunged 1 records
```
