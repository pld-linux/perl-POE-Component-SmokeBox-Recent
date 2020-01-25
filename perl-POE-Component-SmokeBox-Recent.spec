#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	POE
%define	pnam	Component-SmokeBox-Recent
Summary:	POE::Component::SmokeBox::Recent - A POE component to retrieve recent CPAN uploads
Summary(pl.UTF-8):	POE::Component::SmokeBox::Recent - komponent POE odtwarzający ostatnie przesłania do CPAN
Name:		perl-POE-Component-SmokeBox-Recent
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c252c65f6bb3f79d32f079a72da526a2
URL:		http://search.cpan.org/dist/POE-Component-SmokeBox-Recent/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl-POE >= 0.38
BuildRequires:	perl-POE-Component-Client-FTP >= 0.14
BuildRequires:	perl-POE-Component-Client-HTTP >= 0.82
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::SmokeBox::Recent is a POE component for retrieving
recently uploaded CPAN distributions from the CPAN mirror of your
choice.

It accepts a URL and an event name and attempts to download and parse
the RECENT file from that given URL.

It is part of the SmokeBox toolkit for building CPAN Smoke testing
frameworks.

%description -l pl.UTF-8
POE::Component::SmokeBox::Recent to komponent POE do odtwarzania
ostatnich przesłań dystrybucji CPAN z wybranego mirrora CPAN.

Przyjmuje URL i nazwą zdarzenia, próbuje ściągnąć i przeanalizować
plik RECENT z podanego URL-a.

Moduł jest częścią toolkitu SmokeBox do tworzenia szkieletów testowych
CPAN Smoke.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
PERL_MM_USE_DEFAULT=1 \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/SmokeBox/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
