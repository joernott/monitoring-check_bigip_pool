#
# spec file for package monitoring-check_bigip_pool
#

Name:           monitoring-check_bigip_pool
Version:        %{version}
Release:        %{release}
Summary:        Check pool members of F5 bigip load balancer
License:        GPLv3
Group:          System/Monitoring
Url:            https://github.com/joernott/monitoring-check_bigip_pool
Source0:        monitoring-check_bigip_pool-%{version}.tar.gz
BuildArch:      noarch
Requires:       net-snmp-utils

%description
check_bigip_pool is a script using snmpwalk to check if not too many pool
members are down.

%prep
%setup -q -n monitoring-check_bigip_pool-%{version}

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins"
cp check_bigip_pool "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins/"
chmod 0755 "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins/check_bigip_pool"

%files
%attr(755,root,root) /usr/lib64/nagios/plugins/check_bigip_pool

%changelog
* Thu Apr 28 2022 Joern Ott <joern.ott@ott-consult.de>
- Rename repo and standardize rpm builds
* Tue Mar 10 2020 Joern Ott <joern.ott@schufa.de>
- Initial RPM build
