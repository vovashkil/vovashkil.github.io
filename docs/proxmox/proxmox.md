###### back to repo's main [README.md](../../README.md)
# proxmox/ceph
### Proxmox
#### list vm's that are not backed-up
```
pvesh get /cluster/backup-info/not-backed-up
```
### Ceph
#### Remove ceph and config completely in Proxmox
```
systemctl stop ceph-mon.target
systemctl stop ceph-mgr.target
systemctl stop ceph-mds.target
systemctl stop ceph-osd.target
rm -rf /etc/systemd/system/ceph*
killall -9 ceph-mon ceph-mgr ceph-mds
rm -rf /var/lib/ceph/mon/  /var/lib/ceph/mgr/  /var/lib/ceph/mds/
pveceph purge
apt purge ceph-mon ceph-osd ceph-mgr ceph-mds
apt purge ceph-base ceph-mgr-modules-core
rm -rf /etc/ceph/*
rm -rf /etc/pve/ceph.conf
rm -rf /etc/pve/priv/ceph.*
```
#### Removing ceph OSD from system
```
# lsblk | grep -B 1 ceph
sdb                                                                                                     8:16   0   1.7T  0 disk
└─ceph--47bb2e9b--39e8--4632--8532--7b1b633c1017-osd--block--0f51bddd--42ac--4df4--a7fd--14906760668c 252:1    0   1.7T  0 lvm
```
```
# dmsetup remove  ceph--47bb2e9b--39e8--4632--8532--7b1b633c1017-osd--block--0f51bddd--42ac--4df4--a7fd--14906760668c
```
#### Cleaning/wiping LVM configuration for a ceph OSD
```
# lvs | head -2
  LV                                             VG                                        Attr       LSize    Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  osd-block-0f51bddd-42ac-4df4-a7fd-14906760668c ceph-47bb2e9b-39e8-4632-8532-7b1b633c1017 -wi-------   <1.75t
```
```
# lvremove ceph-47bb2e9b-39e8-4632-8532-7b1b633c1017
  Logical volume "osd-block-0f51bddd-42ac-4df4-a7fd-14906760668c" successfully removed.
```
```
# vgremove ceph-47bb2e9b-39e8-4632-8532-7b1b633c1017
  Volume group "ceph-47bb2e9b-39e8-4632-8532-7b1b633c1017" successfully removed
```
```
# pvremove /dev/sdb
  Labels on physical volume "/dev/sdb" successfully wiped.
```
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
