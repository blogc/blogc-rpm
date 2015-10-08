%define real_version 0.2.1

Name:		blogc
Version:	0.2.1
Release:	1%{?dist}
License:	BSD
Group:		Applications/Text
Summary:	A blog compiler
URL:		http://blogc.org/
Source0:	https://github.com/blogc/blogc/releases/download/v%{real_version}/blogc-%{real_version}.tar.xz

#BuildRequires:
#Requires:  

%description
blogc(1) is a blog compiler. It converts source files and templates into
blog/website resources.


%prep
%setup -q -n blogc-%{real_version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_mandir}/man*/blogc*
%{_bindir}/blogc

%doc README.md
%license LICENSE


%changelog
* Wed Sep 16 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.1-1
- First stable release.

* Mon Sep 14 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.1-0.1.beta4
- Initial package.
