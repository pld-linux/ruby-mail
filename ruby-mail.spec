Summary:	RubyMail is a lightweight mail library
Name:		ruby-mail
Version:	1.0.0
Release:	0.1
License:	Ruby License
Source0:	http://rubyforge.org/frs/download.php/30221/rmail-%{version}.tgz
# Source0-md5:	5b104c8519fdf1dcff19368a08d7b300
Group:		Development/Languages
URL:		http://rubyforge.org/projects/rubymail/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
RubyMail is a lightweight mail library.

%package rdoc
Summary:	Documentation files for mail
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for mail.

%prep
%setup -q -n rmail-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
# rm -rf ri/NOT_THIS_MODULE_RELATED_DIRS
rm -f ri/created.rid

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
%doc NEWS NOTES README THANKS TODO
%{ruby_rubylibdir}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/RMail
