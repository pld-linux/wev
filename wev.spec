Summary:	Wayland event viewer
Name:		wev
Version:	1.0.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://git.sr.ht/~sircmpwn/wev/archive/%{version}.tar.gz
# Source0-md5:	202208092a6560b1a78c568996a4cf27
URL:		https://git.sr.ht/~sircmpwn/wev/
BuildRequires:	pkgconfig
BuildRequires:	scdoc
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a tool for debugging events on a Wayland window, analagous to
the X11 tool xev.

%prep
%setup -q

%build
%{__make} all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/wev
%{_mandir}/man1/wev.1*
