Summary:	IPLog - TCP/IP trafic logger
Summary(pl.UTF-8):	IPLog - rejestrator obciążenia sieci pakietami TCP/IP
Name:		iplog
Version:	2.2.3
Release:	3
License:	GPL v2
Group:		Daemons
Source0:	http://dl.sourceforge.net/ojnk/%{name}-%{version}.tar.gz
# Source0-md5:	de98dd64018ab10ebe36e481cf00b7db
Source1:	%{name}.init
Patch0:		%{name}-gcc.patch
URL:		http://ojnk.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Obsoletes:	ippl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iplog is a TCP/IP trafic logger. Currently, it is capable of logging
TCP, UDP and ICMP trafic.

%description -l pl.UTF-8
iplog jest rejestratorem ruchu TCP/IP. Aktualnie może logować ruch
pakietów TCP, UDP i ICMP.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/iplog
install example-iplog.conf $RPM_BUILD_ROOT%{_sysconfdir}/iplog.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add iplog
%service iplog restart "iplog daemon"

%preun
if [ "$0" = "1" ]; then
	%service iplog stop
	/sbin/chkconfig --del iplog
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(754,root,root) /etc/rc.d/init.d/iplog
%attr(755,root,root) %{_sbindir}/iplog
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/iplog.conf
%{_mandir}/man[58]/*
