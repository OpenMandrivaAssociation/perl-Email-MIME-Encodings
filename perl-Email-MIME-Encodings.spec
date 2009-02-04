%define module	    Email-MIME-Encodings
%define name	    perl-%{module}
%define up_version  1.312
%define version     %perl_convert_version %{up_version}
%define release     %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A unified interface to MIME encoding and decoding
License:	GPL or Artistic
Group:		Development/Perl
URL:		    http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.gz
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

