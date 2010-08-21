%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	CompatInfo
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - determine minimal requirements for a program
Summary(pl.UTF-8):	%{_pearname} - określanie minimalnych wymagań programu
Name:		php-pear-%{_pearname}
Version:	1.9.0
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5396bcc77fc7650a73cb0d76b812b7c3
Patch0:		%{name}-cli.patch
Patch1:		PHP_CompatInfo-php53.patch
URL:		http://pear.php.net/package/PHP_CompatInfo/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-Console_GetArgs >= 1.3.3
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
Additional format Renderers for PHP_CompatInfo

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
}' ./%{php_pear_dir}/%{_class}/%{_subclass}/func_array.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

install ./%{_bindir}/pci $RPM_BUILD_ROOT%{_bindir}/pcicmd

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/CompatInfo.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%exclude %{php_pear_dir}/%{_class}/%{_subclass}/Cli.php
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Renderer
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/Null.php

%files Renderers
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/Array.php
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/Csv.php
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/Html.php
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/Text.php
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/Xml.php

# CSS for HTML Renderer
%{php_pear_dir}/data/%{_pearname}

# examples use other Renderers than null, so packaged here
%{_examplesdir}/%{name}-%{version}

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcicmd
%{php_pear_dir}/%{_class}/%{_subclass}/Cli.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
