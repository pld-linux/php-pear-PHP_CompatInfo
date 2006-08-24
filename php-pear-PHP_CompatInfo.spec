%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	CompatInfo
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - determine minimal requirements for a program
Summary(pl):	%{_pearname} - okre¶lanie minimalnych wymagañ programu
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	46981cdc996070cd49f4db3b4bd5a549
Source1:	PHP_CompatInfo.php
URL:		http://pear.php.net/package/PHP_CompatInfo/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
# NB! Console/Table and Console/Getopt are required by CLI

%description
PHP_CompatInfo will parse a file/folder/script/array to find out the
minimum version and extensions required for it to run. Features
advanced debug output which shows which functions require which
version.

In PEAR status of this package is: %{_status}.

%description -l pl
PHP_CompatInfo przetwarza plik/katalog/skrypt/tablicê w celu
okre¶lenia minimalnej wersji i wymaganych rozszerzeñ z jakimi bêdzie
dzia³aæ. Pakiet ten cechuje rozbudowane wy¶wietlanie informacji
diagnostycznych (debug) pokazuj±cych która funkcja wymaga jakiej
wersji.

Ta klasa ma w PEAR status: %{_status}.

%package cli
Summary:	CLI for PHP_CompatInfo
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description cli
CLI for PHP_CompatInfo.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/php-compatinfo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/CompatInfo.php
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}/const_array.php
%{php_pear_dir}/%{_class}/%{_subclass}/func_array.php

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Cli.php
