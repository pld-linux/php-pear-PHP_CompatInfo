%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	CompatInfo
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - determine minimal requirements for a program
Summary(pl):	%{_pearname} - okre¶lanie minimalnych wymagañ programu
Name:		php-pear-%{_pearname}
Version:	0.8.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3a3d9c2b3008c61df8521349fe95a76c
URL:		http://pear.php.net/package/PHP_CompatInfo/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_CompatInfo will parse a file/folder/script/array to find out the
minimum version and extensions required for it to run. Features
advanced debug output which shows which functions require which
version.

This class has in PEAR status: %{_status}.

%description -l pl
PHP_CompatInfo przetwarza plik/katalog/skrypt/tablicê w celu
okreslenia minimalnej wersji i wymaganych rozszereñ z jakimi bêdzie
dzia³aæ. Pakiet ten cechuje rozbudowane wy¶wietlanie informacji
diagnostycznych (debug) pokazuj±cych która funkcja wymaga jakiej
wersji.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/data

install %{_pearname}-%{version}/%{_subclass}*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/data/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/data

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,scripts}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/data
