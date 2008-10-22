# TODO
# - renderers should be optional?
%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	CompatInfo
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - determine minimal requirements for a program
Summary(pl.UTF-8):	%{_pearname} - określanie minimalnych wymagań programu
Name:		php-pear-%{_pearname}
Version:	1.8.1
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a093729a4d205ebc8bf00bcee01de311
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
# NB! Console/Table and Console/Getopt (Console/Getargs) are required by CLI

%description
PHP_CompatInfo will parse a file/folder/script/array to find out the
minimum version and extensions required for it to run. Features
advanced debug output which shows which functions require which
version.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PHP_CompatInfo przetwarza plik/katalog/skrypt/tablicę w celu
określenia minimalnej wersji i wymaganych rozszerzeń z jakimi będzie
działać. Pakiet ten cechuje rozbudowane wyświetlanie informacji
diagnostycznych (debug) pokazujących która funkcja wymaga jakiej
wersji.

Ta klasa ma w PEAR status: %{_status}.

%package cli
Summary:	CLI for PHP_CompatInfo
Summary(pl.UTF-8):	Interfejs linii poleceń dla PHP_CompatInfo
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description cli
CLI for PHP_CompatInfo.

%description cli -l pl.UTF-8
Interfejs linii poleceń dla PHP_CompatInfo.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%patch0 -p1

mv docs/%{_pearname}/docs/examples .

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

install ./%{_bindir}/pci $RPM_BUILD_ROOT%{_bindir}/pcicmd

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/CompatInfo.php
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/data/%{_pearname}

%{_examplesdir}/%{name}-%{version}

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcicmd
%{php_pear_dir}/%{_class}/%{_subclass}/Cli.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
