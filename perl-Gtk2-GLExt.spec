#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pnam	Gtk2-GLExt
Summary:	Gtk2::GLExt - Perl interface to GtkGLExt library
Summary(pl.UTF-8):	Gtk2::GLExt - perlowy interfejs do biblioteki GtkGLExt
Name:		perl-Gtk2-GLExt
Version:	0.92
Release:	1
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	597cda879004ac1fc3023e80f66946c6
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gtkglext-devel >= 1.0
BuildRequires:	perl-ExtUtils-Depends >= 0.2
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib-devel >= 1.060
BuildRequires:	perl-Gtk2-devel >= 1.060
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	gtkglext >= 1.0
Requires:	perl-Glib >= 1.060
Requires:	perl-Gtk2 >= 1.060
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk2::GLExt module allows a Perl developer to use GtkGLExt, an
OpenGL extension to GTK+ by Naofumi Yasufuku, with perl-Gtk2.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Moduł Gtk2::GLExt pozwala programistom perlowym używać GtkGLExt
(rozszerzenia OpenGL dla GTK+ autorstwa Naofumi Yasufuku) wraz z
modułem perl-Gtk2.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gtk2-GLExt bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gtk2-GLExt dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	gtkglext-devel >= 1.0
Requires:	perl-Cairo-devel
Requires:	perl-Glib-devel >= 1.060
Requires:	perl-Gtk2-devel >= 1.060

%description devel
Development files for Perl Gtk2-GLExt bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gtk2-GLExt dla Perla.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/GLExt.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/GLExt/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/Gdk/GLExt/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{perl_vendorarch}/Gtk2/GLExt.pm
%dir %{perl_vendorarch}/Gtk2/GLExt
%dir %{perl_vendorarch}/auto/Gtk2/GLExt
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/GLExt/GLExt.so
%{_mandir}/man3/Gtk2::GLExt*.3pm*
%{_mandir}/man3/Gtk2::Gdk::GLExt*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/GLExt/Install
