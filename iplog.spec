Summary:	IPLog - TCP/IP trafic logger.
Summary(pl):	IPLog - rejestrator obci±¿enia sieci pakietami TCP/IP
Name:		iplog
Version:	2.1.0
Release:	1
Copyright:	GPL
Group:		Daemons
Group(pl):	Demony
Source:		http://www.numb.org/~odin/stuff/%name-%version.tar.gz
#Patch:		
BuildRequires:	libpcap
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
iplog is a TCP/IP trafic logger.
Currently, it is capable of logging TCP, UDP and ICMP trafic.

%description -l pl

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} \
    man5dir=$RPM_BUILD_ROOT%{_mandir}/man5 \
    man8dir=$RPM_BUILD_ROOT%{_mandir}/man8 \
     install

install -d $RPM_BUILD_ROOT/etc
cp example-iplog.rules $RPM_BUILD_ROOT/etc/iplog.rules

gzip -9 $RPM_BUILD_ROOT%{_mandir}/{man5,man8}/*
gzip -9 README AUTHORS NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS,TODO,AUTHORS}.gz
%config(noreplace) %attr(600,root,root) /etc/iplog.rules
%attr(755,root,root) %{_sbindir}/iplog
%attr(644, root,root) %{_mandir}/man5/*.gz
%attr(644, root,root) %{_mandir}/man8/*.gz
