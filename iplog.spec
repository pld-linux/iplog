Summary:	IPLog - TCP/IP trafic logger
Summary(pl):	IPLog - rejestrator obci±¿enia sieci pakietami TCP/IP
Name:		iplog
Version:	2.2.3
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://www.numb.org/~odin/stuff/%{name}-%{version}.tar.gz
# Source0-md5:	ab1540c60a28d232e2c562f94845816b
Source1:	%{name}.init
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
PreReq:		/sbin/chkconfig
PreReq:		rc-scripts
Obsoletes:	ippl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iplog is a TCP/IP trafic logger. Currently, it is capable of logging
TCP, UDP and ICMP trafic.

%description -l pl
iplog jest rejestratorem ruchu TCP/IP. Aktualnie mo¿e logowaæ ruch
pakietów TCP, UDP i ICMP.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/iplog
install example-iplog.conf $RPM_BUILD_ROOT%{_sysconfdir}/iplog.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add iplog
if [ -f /var/lock/subsys/iplog ]; then
	/etc/rc.d/init.d/iplog restart >&2
else
	echo "Run \"/etc/rc.d/init.d/iplog start\" to start iplog daemon."
fi

%preun
if [ "$0" = "1" ]; then
	if [ -f /var/lock/subsys/iplog ]; then
		/etc/rc.d/init.d/iplog stop >&2
	fi
	/sbin/chkconfig --del iplog
fi

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO
%attr(754,root,root) /etc/rc.d/init.d/iplog
%attr(755,root,root) %{_sbindir}/iplog
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/iplog.conf
%{_mandir}/man[58]/*
