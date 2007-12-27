%define module	Dict-FSA
%define name	perl-%{module}
%define version 0.1.2
%define release %mkrel 2

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    FSA wrapper
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}/
Source:		    http://search.cpan.org/CPAN/authors/id/G/GR/GROUSSE/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	fsa
Requires:	    fsa
Buildarch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This module is a perl wrapper around fsa, a set of tools based on finite state
automata.

%prep
%setup -q -n %{module}-%{version}

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
%doc README ChangeLog
%{perl_vendorlib}/Dict
%{_mandir}/*/*
