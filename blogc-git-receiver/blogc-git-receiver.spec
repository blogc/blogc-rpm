%define real_version 0.1-beta.5

Name:		blogc-git-receiver
Version:	0.1
Release:	0.1.beta5%{?dist}
License:	BSD
Group:		System Environment/Shells
Summary:	A simple login shell/git hook to deploy blogc websites
URL:		http://blogc.org/
Source0:	https://github.com/blogc/blogc-git-receiver/releases/download/v%{real_version}/blogc-git-receiver-%{real_version}.tar.xz

BuildRequires:	git, tar, make
Requires:	git, tar, make

%description
blogc-git-receiver is a simple login shell/git hook to deploy blogc websites

%prep
%setup -q -n blogc-git-receiver-%{real_version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_bindir}/blogc-git-receiver

%doc README.md
%license LICENSE


%changelog
* Mon Sep 14 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.1-0.1.beta5
- Initial package.
