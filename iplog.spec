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
Buildroot:	/tmp/%{name}-%{version}-root

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
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
