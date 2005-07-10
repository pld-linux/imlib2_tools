Summary:	Clone of ImageMagick command line programs using Imlib2
Name:		imlib2_tools
Version:	0.0.0alpha2
%define	_snap	20050701
Release:	0.%{_snap}.0.1
License:	BSD
Group:		Applications/Graphics
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/apps/%{name}-%{_snap}.tar.gz
# Source0-md5:	588212cac24c27f6987e9c0d73940012
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clone of ImageMagick command line programs using Imlib2.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING TODO
%attr(755,root,root) %{_bindir}/imlib2_convert
%attr(755,root,root) %{_bindir}/imlib2_identify
