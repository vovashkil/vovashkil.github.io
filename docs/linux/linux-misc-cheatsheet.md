# Some useful linux/unix cli commands and more

* back to repo's main [README.md](../../README.md)

## cheatsheet-linux-misc

### write a read-only file in vi

```vi
:w !sudo tee %
```

### my ip origin look-up

```bash
curl icanhazip.com
```

### journalctl log file retention

Retain only the past two days:

```bash
journalctl --vacuum-time=2d
```

Retain only the past 500 MB:

```bash
journalctl --vacuum-size=500M
```

### Re-scan SCSI bus when a hot swap drive is inserted (tested on debian & SuperMicro)

```shell
lsblk # check available block devices in the system
cd /sys/class/scsi_host
for i in *; do echo '- - -' > $i/scan; done # send re-scan command to the bus
lsblk # re-check available block devices in the system after the re-scan
```

### nfs performance measuring

```bash
sudo fio --name=fio-efs --filesize=2G --filename=./efs/fio-efs-test.img --bs=1M --nrfiles=1 --direct=1 --sync=0 --rw=write --iodepth=200 --ioengine=libaio
```

### ldap monitoring contextCSN

```bash
ldapsearch  -z 1 -H ldaps://ldap.example.com  -LLL -b 'dc=example,dc=com' -s base -x contextCSN
```

ldap server id's are 111 and 222 in the output:

```bash
dn: dc=example,dc=com
contextCSN: 20231011231244.659412Z#000000#111#000000
contextCSN: 20240322195804.558951Z#000000#222#000000
```

### ping: socket: Operation not permitted

```bash
chmod 4711 `which ping`
```

### when "apt --fix-broken install" doesn't work

This could happen when there are problems with dependencies when installing/removing packages.
Double check the output of the following command:

```bash
dpkg --configure -a
dpkg: dependency problems prevent configuration of package_XXX:i386:
 package_XXX:i386 depends on package_YYY (= <version>); however:
  Package package_YYY:i386 is not installed.
```

Then run the following for all packages having problems:

```bash
dpkg --force depends -P package_XXX
```

And in the end try again:

```bash
apt --fix-broken install
```

### Change Default Network Name (ens33) to eth0

#### On Debian 10 / Debian 9 (this doesn't work in Debian 11(bullseye))

1\. Apply the change to /etc/default/grub

```bash
GRUB_CMDLINE_LINUX="" -> GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0"
```

2\. Update grub

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

3\. change interfaces name to eth0, eth1, ... in /etc/network/interfaces, /etc/network/interfaced.d/*
4\. Reboot

```bash
reboot
```

#### On Debian 12

1\. Create corresponding files under `/etc/systemd/network/`

```bash
$ cat /etc/systemd/network/10-eth0.link
[Match]
MACAddress=bc:24:11:5d:ee:95
[Link]
Name=eth0
```

### SSL certificate basic checks

#### SSL certificate end date

```bash
openssl x509 -enddate -noout -in server.crt
```

or on a remote system

```bash
echo | openssl s_client -showcerts -servername gnupg.org -connect gnupg.org:443 2>/dev/null | openssl x509 -inform pem -noout -dates
```

#### SSL certificate and prtivate key match

```bash
openssl x509 -noout -modulus -in server.crt | openssl md5
openssl rsa -noout -modulus -in server.key | openssl md5
```

#### SSL Convert from P7B to PEM via OpenSSL

```bash
openssl pkcs7 -in cert.p7b -inform DER -print_certs -out cert.pem
```

### Configure 802.1Q VLAN Tagging

* **NB! Doing this (native vlan + tagged vlan in a bridge) on more than 1 node in a cluster will cause broadcast storm due to l2 loop**

```bash
ip link add link bond0 name bond0.10 type vlan id 10
ip link set bond0.10 up
brctl addif vmbr0 bond0.10
ip addr add 10.10.10.10/24 dev vmbr0 label vmbr0:10
```

### DRBD Split Brain

* **Choose one node and run**

```bash
drbdadm secondary all
drbdadm disconnect all
drbdadm -- --discard-my-data connect all
```

* **Make other node primary**

```bash
drbdadm primary all
drbdadm disconnect all
drbdadm connect all
```

* **Check /proc/drbd again**

### IPMI

```bash
ipmitool -I lanplus -H 10.10.10.10 -U ADMIN sol activate
```

### tcpdump

```bash
tcpdump -p -n -i external -s 1500 -l -x -X -c 1000000 -w /tmp/foo.dump
```

### zabbix server reset auth to default one if ldap is broken, default creds: Admin/zabbix

```bash
sudo -u zabbix psql
zabbix=>  update config set authentication_type=0 ;
 UPDATE 1
```

### Add Secondary IP Address To CentOS / RHEL Network Interface

/etc/sysconfig/network-scripts/ifcfg-eth0:1

```bash
DEVICE=eth0:1
Type=Ethernet
ONBOOT=yes
NM_CONTROLLED=no
BOOTPROTO=none
IPADDR=10.10.10.11
PREFIX=24
```

### Check snmp is working with get uptime

```bash
snmpwalk -v2c -c public  10.10.10.10 1.3.6.1.2.1.1.3
```

### syslog access to kea logs

```bash
sudo apt install acl
sudo setfacl -R -m u:root:rx /var/log/kea/
```

### dnsdist access letsencrrypt certs

```bash
sudo apt install acl
sudo setfacl -R -m u:_dnsdist:rx /etc/letsencrypt/
sudo dnsdist --check-config
```

### access letsencrrypt certs with salt

```yaml
ldap-access-to-machine-live-dir:
  acl.present:
    - name: /etc/letsencrypt/live
    - acl_type: user
    - acl_name: openldap
    - perms: rx

ldap-access-to-machine-archive-dir:
  acl.present:
    - name: /etc/letsencrypt/archive
    - acl_type: user
    - acl_name: openldap
    - perms: rx
```

### dnsdist access letsencrrypt certs destination

* Source: [www.server-world.info](https://www.server-world.info/en/note?os=Debian_10&p=acl)

### Error with skype installation on ubuntu

* **Error:**

```bash
Err:9 https://repo.skype.com/deb stable InRelease                        
The following signatures were invalid: EXPKEYSIG 1F3045A5DF7587C3 Skype Linux Client Repository <se-um@microsoft.com>
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG ### error: https://repo.skype.com/deb stable InRelease: The following signatures were invalid: EXPKEYSIG 1F3045A5DF7587C3 Skype Linux ### Client Repository <se-um@microsoft.com>
```

```bash
apt-key del EXPKEYSIG
curl https://repo.skype.com/data/SKYPE-GPG-KEY | sudo apt-key add -
```

### Removing a repo in ubuntu

* **Error:**

```bash
E: The repository 'http://ppa.launchpad.net/phablet-team/tools/ubuntu bionic Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

```bash
apt-add-repository -r ppa:phablet-team/tools # remove the repo
```

### graylog/elasticsearch doesn't recover after out of free disk space event 

* Source: [community.graylog.org](https://community.graylog.org/t/graylog-not-processing-messages-processing-buffer-full/15987)

```bash
curl -XPUT -H "Content-Type: application/json" http://[YOUR_ELASTICSEARCH_ENDPOINT]:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'
```

### Misc/General troubleshooting

```bash
iostat -cx 2 | logger -t iostat.log -p user.error &
watch cat /proc/meminfo | logger -t meminfo.log -p user.error &
watch free -m | logger -t free_mem.log -p user.error &
watch top -b -n1 | logger -t top.log -p user.error &
```
