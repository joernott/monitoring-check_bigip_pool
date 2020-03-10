#
# spec file for package icinga_check_bigip_pool
#

Name:           icinga_check_bigip_pool
Version:        %{version}
Release:        %{release}
Summary:        Check pool members of F5 bigip load balancer
License:        GPLv3
Group:          System/Monitoring
Url:            https://github.com/joernott/check_bigip_pool
Source0:        https://github.com/joernott/check_bigip_pool/releases/download/%{version}/check_bigip_pool-%{version}.tar.gz
BuildArch:      noarch
Requires:       net-snmp-utils

%description
check_bigip_pool is a script using snmpwalk to check if not too many pool
members are down.

%prep
%setup -q -n check_bigip_pool-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib64/nagios/plugins
cp check_bigip_pool $RPM_BUILD_ROOT/usr/lib64/nagios/plugins/

%files
%defattr(-,root,root,755)
/usr/lib64/nagios/plugins/check_bigip_pool

%changelog
* Tue Mar 10 2020 Joern Ott <joern.ott@schufa.de>
- Initial RPM build
