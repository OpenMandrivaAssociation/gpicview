Summary:	A Simple and Fast Image Viewer for X
Name:     	gpicview
Version:	0.2.5
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://www.lxde.org/
Source0: 	http://sourceforge.net/project/lxde/%name-%version.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	intltool >= 0.40.0
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(gtk+-2.0)

%description
GPicView is a simple and fast image viewer for X.
It features:
. Extremely lightweight and fast with low memory usage
. Very suitable for default image viewer of desktop system
. Simple and intuitive interface
. Minimal lib dependency: Only pure GTK+ is used
. Desktop independent: Doesn't require any specific desktop environment

%prep
%setup -q

%build
%configure
%make_build LIBS="-ljpeg -lm"

%install
%make_install

%find_lang %{name}

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--remove-category='Application' \
	--remove-category='Core' \
	--remove-category='Utility' \
	--remove-category='Photography' \
	--remove-category='RasterGraphics' \
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/*

