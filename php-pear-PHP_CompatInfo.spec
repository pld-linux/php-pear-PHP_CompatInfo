%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	PHP_CompatInfo
Summary:	%{_pearname} - determine minimal requirements for a program
Summary(pl.UTF-8):	%{_pearname} - określanie minimalnych wymagań programu
Name:		php-pear-%{_pearname}
Version:	1.9.0
Release:	5
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5396bcc77fc7650a73cb0d76b812b7c3
Patch0:		%{name}-cli.patch
Patch1:		PHP_CompatInfo-php53.patch
URL:		http://pear.php.net/package/PHP_CompatInfo/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-Console_Getargs >= 1.3.3
Requires:	php-pear-Console_Table >= 1.1.1
Requires:	php-pear-Event_Dispatcher >= 1.0.0
Requires:	php-pear-File_Find >= 1.3.0
Requires:	php-pear-PEAR-core >= 1:1.5.4
Requires:	php-tokenizer
Suggests:	php-pear-Console_ProgressBar
Suggests:	php-pear-HTML_Table
Suggests:	php-pear-PHPUnit
Suggests:	php-pear-Var_Dump
Suggests:	php-pear-XML_Beautifier
Suggests:	php-pear-XML_Util
Obsoletes:	php-pear-PHP_CompatInfo-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
# NB! Console/Table and Console/Getopt (Console/Getargs) are required by CLI
%define		_noautoreq	pear(Console/ProgressBar.*) pear(HTML/Table.*) pear(PHPUnit.*) pear(Var/Dump.*) pear(XML/Beautifier.*) pear(XML/Util.*)

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

# could make subpkg for each, but that's imho overkill, just want base package
# being minimal for rpm-php-pearprov.
%package Renderers
Summary:	Additional format Renderers for PHP_CompatInfo
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Renderers
Additional format Renderers for PHP_CompatInfo.

%prep
%pear_package_setup
%patch0 -p1
%patch1 -p1

mv docs/%{_pearname}/docs/examples .

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

# pld package names
%{__sed} -i -e '/ext/{
	s/pecl_http/pecl-http/
	s/apc/pecl-APC/
	s/fileinfo/pecl-fileinfo/
}' ./%{php_pear_dir}/PHP/CompatInfo/func_array.php

# used by pciconf, move to datadir
install -d ./%{php_pear_dir}/data/%{_pearname}
mv ./%{_bindir}/scripts ./%{php_pear_dir}/data/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PHP/CompatInfo.php
%{php_pear_dir}/PHP/CompatInfo/*.php
%exclude %{php_pear_dir}/PHP/CompatInfo/Cli.php
%dir %{php_pear_dir}/PHP/CompatInfo
%dir %{php_pear_dir}/PHP/CompatInfo/Renderer
%{php_pear_dir}/PHP/CompatInfo/Renderer/Null.php
%dir %{php_pear_dir}/data/%{_pearname}

%files Renderers
%defattr(644,root,root,755)
%{php_pear_dir}/PHP/CompatInfo/Renderer/Array.php
%{php_pear_dir}/PHP/CompatInfo/Renderer/Csv.php
%{php_pear_dir}/PHP/CompatInfo/Renderer/Html.php
%{php_pear_dir}/PHP/CompatInfo/Renderer/Text.php
%{php_pear_dir}/PHP/CompatInfo/Renderer/Xml.php

# CSS for HTML Renderer
%{php_pear_dir}/data/%{_pearname}/pci.css

# examples use other Renderers than null, so packaged here
%{_examplesdir}/%{name}-%{version}

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pci
%attr(755,root,root) %{_bindir}/pciconf
%{php_pear_dir}/PHP/CompatInfo/Cli.php

# data for pciconf
%{php_pear_dir}/data/%{_pearname}/scripts
%{php_pear_dir}/data/%{_pearname}/data
