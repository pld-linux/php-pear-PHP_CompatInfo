%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	CompatInfo
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - determine minimal requirements for a program
Summary(pl):	%{_pearname} - okre�lanie minimalnych wymaga� programu
Name:		php-pear-%{_pearname}
Version:	1.3.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1198ca0995f7d75336b90d786253de5e
Patch0:		%{name}-cli.patch
URL:		http://pear.php.net/package/PHP_CompatInfo/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(tokenizer)
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
PHP_CompatInfo przetwarza plik/katalog/skrypt/tablic� w celu
okre�lenia minimalnej wersji i wymaganych rozszerze� z jakimi b�dzie
dzia�a�. Pakiet ten cechuje rozbudowane wy�wietlanie informacji
diagnostycznych (debug) pokazuj�cych kt�ra funkcja wymaga jakiej
wersji.

Ta klasa ma w PEAR status: %{_status}.

%package cli
Summary:	CLI for PHP_CompatInfo
Summary(pl):	Interfejs linii polece� dla PHP_CompatInfo
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description cli
CLI for PHP_CompatInfo.

%description cli -l pl
Interfejs linii polece� dla PHP_CompatInfo.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

mv $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/pcicmd.php $RPM_BUILD_ROOT%{_bindir}/pcicmd
chmod +x $RPM_BUILD_ROOT%{_bindir}/pcicmd

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
%{php_pear_dir}/%{_class}/%{_subclass}/Cli.php
