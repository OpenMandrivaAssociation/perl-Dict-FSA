%define module	Dict-FSA

Name:		perl-%{module}
Version:	0.1.2
Release:	7
Summary:	FSA wrapper
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://search.cpan.org/CPAN/authors/id/G/GR/GROUSSE/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	fsa
Requires:	fsa
BuildArch:	noarch

%description
This module is a perl wrapper around fsa, a set of tools based on finite state
automata.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README ChangeLog
%{perl_vendorlib}/Dict
%{_mandir}/*/*

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.1.2-6mdv2011.0
+ Revision: 681408
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.2-5mdv2011.0
+ Revision: 430411
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-4mdv2009.0
+ Revision: 256676
- rebuild

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-2mdv2008.1
+ Revision: 138295
- add missing spec file in repository

  + Thierry Vignaud <tv@mandriva.org>
    - import perl-Dict-FSA


* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-1mdv2007.0
- new version

* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-2mdv2007.0
- Rebuild

* Sun Nov 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdk
- first mdk release
