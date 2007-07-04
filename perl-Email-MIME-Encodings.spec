%define module	Email-MIME-Encodings
%define name	perl-%{module}
%define version 1.31.1
%define up_version 1.311
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A unified interface to MIME encoding and decoding
License:	GPL or Artistic
Group:		Development/Perl
URL:		    http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module simply wraps MIME::Base64 and MIME::QuotedPrint so that you can
throw the contents of a Content-Transfer-Encoding header at some text and have
the right thing happen.
Provides a number of useful methods for manipulating MIME messages.

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*

