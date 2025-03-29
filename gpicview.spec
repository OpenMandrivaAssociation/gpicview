# git snapshot
#global snapshot 1
%if 0%{?snapshot}
	%global commit		4dbf512562ff00df2c3476f52f1e568d7c873090
	%global commitdate	20249005
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	A Simple and Fast Image Viewer for X
Name:     	gpicview
Version:	0.3.1
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		https://www.lxde.org/
#Source0: 	http://sourceforge.net/project/lxde/%name-%version.tar.xz
Source0:	https://github.com/lxde/gpicview/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	intltool >= 0.40.0
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(gtk+-3.0)

%description
GPicView is a simple and fast image viewer for X.
It features:
. Extremely lightweight and fast with low memory usage
. Very suitable for default image viewer of desktop system
. Simple and intuitive interface
. Minimal lib dependency: Only pure GTK+ is used
. Desktop independent: Doesn't require any specific desktop environment

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	--enable-dbus \
	--enable-gtk3 \
	%{nil}
%make_build
# LIBS="-ljpeg -lm"

%install
%make_install

# locales
%find_lang %{name}

# .desktop
desktop-file-install \
	--vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--remove-category='Application' \
	--remove-category='Core' \
	--remove-category='Utility' \
	--remove-category='Photography' \
	--remove-category='RasterGraphics' \
	%{buildroot}%{_datadir}/applications/*.desktop

