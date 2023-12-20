###### back to repo's main [README.md](../../README.md)
# DHCP misc
### Monitoring traffic @ MX
```
user@bng-router> monitor traffic no-resolve layer2-headers detail interface ps474
```
### Clear a Subscriber
maint node:
```
user@maint:~$ curl --location --request POST 'http://dhcp.domain.com:8080' --header 'Content-Type: application/json' --data-raw '{"command": "lease4-del", "service": ["dhcp4"], "arguments": {"ip-address": "10.10.10.111"} }'
[ { "result": 0, "text": "IPv4 lease deleted." } ]
```
```
user@bng-router> show subscribers stacked-vlan-id XXX vlan-id YYYY    
Total subscribers: 0, Active Subscribers: 0
```
