%define pkgname mail
Summary:	A Really Ruby Mail Library 
Name:		ruby-%{pkgname}
Version:	2.1.3
Release:	2
License:	BSD-like
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	b9bc3bb5d8ea876b016976f6f1fe5ac4
Patch0:		%{name}-vendor.patch
Group:		Development/Languages
URL:		http://github.com/mikel/mail
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-activesupport
Requires:	ruby-mime-types
Requires:	ruby-treetop
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
A Really Ruby Mail Library.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.rdoc -o -print | xargs touch --reference %{SOURCE0}
%patch0 -p1

rm -r lib/mail/vendor

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm -r ri/{NilClass,String}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rdoc README.rdoc TODO.rdoc
%{ruby_rubylibdir}/mail.rb
%{ruby_rubylibdir}/mail
%{ruby_rubylibdir}/tasks

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Mail
