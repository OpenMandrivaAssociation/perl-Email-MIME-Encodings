%define module	    Email-MIME-Encodings
%define upstream_version 1.315

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	A unified interface to MIME encoding and decoding
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Email/Email-MIME-Encodings-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Capture::Tiny)
BuildArch:	noarch

%description
This module simply wraps MIME::Base64 and MIME::QuotedPrint so that you can
throw the contents of a Content-Transfer-Encoding header at some text and have
the right thing happen.
Provides a number of useful methods for manipulating MIME messages.

%prep
%setup -q -n %{module}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*

%changelog
* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.313.0-1mdv2010.0
+ Revision: 377826
- new version
- new release
- standardised version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.31.1-3mdv2009.0
+ Revision: 241211
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.31.1-1mdv2008.0
+ Revision: 48065
- update to new version 1.311


* Thu Sep 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.31.0-1mdv2007.0
- new version

* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-2mdv2007.0
- Rebuild

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-1mdk
- first mdk release



