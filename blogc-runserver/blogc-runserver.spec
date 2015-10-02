%define real_version 0.1

Name:		blogc-runserver
Version:	0.1
Release:	1%{?dist}
License:	BSD
Group:		Development/Tools
Summary:	A simple HTTP server to test blogc websites
URL:		http://blogc.org/
Source0:	https://github.com/blogc/blogc-runserver/releases/download/v%{real_version}/blogc-runserver-%{real_version}.tar.xz

BuildRequires:	libevent-devel >= 2.0, file-devel 
Requires:	libevent >= 2.0, file-libs

%description
blogc-runserver is a simple HTTP server to test blogc websites

%prep
%setup -q -n blogc-runserver-%{real_version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_bindir}/blogc-runserver

%doc README.md
%license LICENSE


%changelog
* Fri Oct 2 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.1-1
- Initial package.
