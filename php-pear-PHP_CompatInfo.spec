%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	CompatInfo
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - determine minimal requirements for a program
Summary(pl):	%{_pearname} - okre¶lanie minimalnych wymagañ programu
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ede40f01b25e76ddc87beed18adc7065
URL:		http://pear.php.net/package/PHP_CompatInfo/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Console/Table.*)' 'pear(Console/Getopt.*)'

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

%prep
%pear_package_setup

# fix hierarchy
mv ./%{php_pear_dir}/%{_class}/scripts docs
install -d ./%{php_pear_dir}/data
mv ./%{php_pear_dir}/{%{_class}/data,data/%{_pearname}}
sed -i -e 's,%{_class}/data,data/%{_pearname},' ./%{php_pear_dir}/%{_class}/%{_subclass}.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%doc docs/scripts
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%{php_pear_dir}/data/%{_pearname}
