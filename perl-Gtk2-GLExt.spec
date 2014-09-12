#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Gtk2-GLExt
Summary:	Gtk2::GLExt - Perl interface to GtkGLExt library
Summary(pl.UTF-8):	Gtk2::GLExt - perlowy interfejs do biblioteki GtkGLExt
Name:		perl-Gtk2-GLExt
Version:	0.90
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	828adc4e963518978e81c4e099dd1e5c
Patch0:		%{name}-fix.patch
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gtkglext-devel >= 1.0
BuildRequires:	perl-ExtUtils-Depends >= 0.2
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Glib >= 1.060
BuildRequires:	perl-Gtk2 >= 1.060
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gtkglext >= 1.0
Requires:	perl-Glib >= 1.060
Requires:	perl-Gtk2 >= 1.060
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk2::GLExt module allows a Perl developer to use GtkGLExt, an
OpenGL extension to GTK+ by Naofumi Yasufuku, with perl-Gtk2.

%description -l pl.UTF-8
Moduł Gtk2::GLExt pozwala programistom perlowym używać GtkGLExt
(rozszerzenia OpenGL dla GTK+ autorstwa Naofumi Yasufuku) wraz z
modułem perl-Gtk2.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

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

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/GLExt.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/GLExt/*.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/Gdk/GLExt/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{perl_vendorarch}/Gtk2/GLExt.pm
%dir %{perl_vendorarch}/Gtk2/GLExt
%{perl_vendorarch}/Gtk2/GLExt/Install
%dir %{perl_vendorarch}/auto/Gtk2/GLExt
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/GLExt/GLExt.so
%{_mandir}/man3/Gtk2::GLExt*.3pm*
%{_mandir}/man3/Gtk2::Gdk::GLExt*.3pm*
