###### back to repo's main [README.md](../../README.md)
# proxmox/ceph
### Proxmox
#### list vm's that are not backed-up
```
pvesh get /cluster/backup-info/not-backed-up
```
### Ceph
#### Ceph Crash
```
ceph crash ls
ceph crash info <id>
ceph crash archive <id>
```
or:
```
ceph crash archive-all
```
#### ceph warning after ceph upgrade
Source: [forum.proxmox.com link](https://forum.proxmox.com/threads/ceph-nautilus-and-octopus-security-update-for-insecure-global_id-reclaim-cve-2021-20288.88038/)
```
systemctl try-reload-or-restart pvestatd.service pvedaemon.service
ceph config set mon auth_allow_insecure_global_id_reclaim false
```
