Summary:	IPLog - TCP/IP trafic logger.
Summary(pl):	IPLog - rejestrator obci±¿enia sieci pakietami TCP/IP
Name:		iplog
Version:	2.2.1
Release:	1
License:	GPL
Group:		Daemons
Group(pl):	Serwery
Source0:	http://www.numb.org/~odin/stuff/%{name}-%{version}.tar.gz
Source1:	%{name}.init
BuildRequires:	libpcap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
iplog is a TCP/IP trafic logger. Currently, it is capable of logging
TCP, UDP and ICMP trafic.

%description -l pl

%prep
%setup -q
%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT 

install -d $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/iplog

cp example-iplog.conf $RPM_BUILD_ROOT%{_sysconfdir}/iplog.conf

gzip -9nf README AUTHORS NEWS TODO

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS,TODO,AUTHORS}.gz
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/iplog
%attr(755,root,root) %{_sbindir}/iplog
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/iplog.conf
%{_mandir}/man[58]/*
