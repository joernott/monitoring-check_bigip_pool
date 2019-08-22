# Nagios/Icinga check for F5 BigIP loadbalancer pools

A simple bash script using snmpwalk to check if not too many pool members are
down.

## Usage
```
    check_bigip_pool -A <address> -p <pool> -w <warn> -c <critical>

       Checks the pool <pool> (case sensitive) on the bigip <address.
       If less than <warn> servers are down, it returns OK, otherwise
       warn (>= <warn> and <= <critical>) or critical (>= <critical>).
```

## Installation
1. Install net-snmp or whatever package conatins snmpwalk

2. Copy the script into your plugin directory.

3. Download the MIB archive from your F5 loadbalancer (See help menu) and place
the files in /usr/share/snmp/mibs.

4. Create command configuration in Icinga2 or Nagios

## Legal

### License
Gnu Public License v3

### Author
Jörn Ott <joern.ott@ott-consult.de>
