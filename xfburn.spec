#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfburn
Version  : 0.6.0
Release  : 6
URL      : http://archive.xfce.org/src/apps/xfburn/0.6/xfburn-0.6.0.tar.bz2
Source0  : http://archive.xfce.org/src/apps/xfburn/0.6/xfburn-0.6.0.tar.bz2
Summary  : A simple CD/DVD burning tool based on libburnia libraries
Group    : Development/Tools
License  : GPL-2.0
Requires: xfburn-bin = %{version}-%{release}
Requires: xfburn-data = %{version}-%{release}
Requires: xfburn-license = %{version}-%{release}
Requires: xfburn-locales = %{version}-%{release}
Requires: xfburn-man = %{version}-%{release}
BuildRequires : exo-dev
BuildRequires : intltool
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gstreamer-pbutils-1.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libburn-1)
BuildRequires : pkgconfig(libisofs-1)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : util-linux

%description
==============================================================================
xfburn
------

%package bin
Summary: bin components for the xfburn package.
Group: Binaries
Requires: xfburn-data = %{version}-%{release}
Requires: xfburn-license = %{version}-%{release}

%description bin
bin components for the xfburn package.


%package data
Summary: data components for the xfburn package.
Group: Data

%description data
data components for the xfburn package.


%package license
Summary: license components for the xfburn package.
Group: Default

%description license
license components for the xfburn package.


%package locales
Summary: locales components for the xfburn package.
Group: Default

%description locales
locales components for the xfburn package.


%package man
Summary: man components for the xfburn package.
Group: Default

%description man
man components for the xfburn package.


%prep
%setup -q -n xfburn-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572809227
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1572809227
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfburn
cp %{_builddir}/xfburn-0.6.0/COPYING %{buildroot}/usr/share/package-licenses/xfburn/dfac199a7539a404407098a2541b9482279f690d
%make_install
%find_lang xfburn

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfburn

%files data
%defattr(-,root,root,-)
/usr/share/Thunar/sendto/thunar-sendto-xfburn.desktop
/usr/share/appdata/xfburn.appdata.xml
/usr/share/applications/xfburn.desktop
/usr/share/icons/hicolor/16x16/stock/media/stock_xfburn-audio-cd.png
/usr/share/icons/hicolor/16x16/stock/media/stock_xfburn-blank-cdrw.png
/usr/share/icons/hicolor/16x16/stock/media/stock_xfburn-burn-cd.png
/usr/share/icons/hicolor/16x16/stock/media/stock_xfburn-data-copy.png
/usr/share/icons/hicolor/16x16/stock/media/stock_xfburn-import-session.png
/usr/share/icons/hicolor/16x16/stock/media/stock_xfburn-new-data-composition.png
/usr/share/icons/hicolor/16x16/stock/media/stock_xfburn.png
/usr/share/icons/hicolor/22x22/stock/media/stock_xfburn-audio-cd.png
/usr/share/icons/hicolor/22x22/stock/media/stock_xfburn-blank-cdrw.png
/usr/share/icons/hicolor/22x22/stock/media/stock_xfburn-burn-cd.png
/usr/share/icons/hicolor/22x22/stock/media/stock_xfburn-data-copy.png
/usr/share/icons/hicolor/22x22/stock/media/stock_xfburn-import-session.png
/usr/share/icons/hicolor/22x22/stock/media/stock_xfburn-new-data-composition.png
/usr/share/icons/hicolor/22x22/stock/media/stock_xfburn.png
/usr/share/icons/hicolor/24x24/stock/media/stock_xfburn-audio-cd.png
/usr/share/icons/hicolor/24x24/stock/media/stock_xfburn-audio-copy.png
/usr/share/icons/hicolor/24x24/stock/media/stock_xfburn-blank-cdrw.png
/usr/share/icons/hicolor/24x24/stock/media/stock_xfburn-burn-cd.png
/usr/share/icons/hicolor/24x24/stock/media/stock_xfburn-data-copy.png
/usr/share/icons/hicolor/24x24/stock/media/stock_xfburn-format-dvdrw.png
/usr/share/icons/hicolor/24x24/stock/media/stock_xfburn-import-session.png
/usr/share/icons/hicolor/24x24/stock/media/stock_xfburn-new-data-composition.png
/usr/share/icons/hicolor/24x24/stock/media/stock_xfburn.png
/usr/share/icons/hicolor/32x32/stock/media/stock_xfburn-audio-cd.png
/usr/share/icons/hicolor/32x32/stock/media/stock_xfburn-blank-cdrw.png
/usr/share/icons/hicolor/32x32/stock/media/stock_xfburn-burn-cd.png
/usr/share/icons/hicolor/32x32/stock/media/stock_xfburn-data-copy.png
/usr/share/icons/hicolor/32x32/stock/media/stock_xfburn-import-session.png
/usr/share/icons/hicolor/32x32/stock/media/stock_xfburn-new-data-composition.png
/usr/share/icons/hicolor/32x32/stock/media/stock_xfburn.png
/usr/share/icons/hicolor/48x48/stock/media/stock_xfburn-audio-cd.png
/usr/share/icons/hicolor/48x48/stock/media/stock_xfburn-blank-cdrw.png
/usr/share/icons/hicolor/48x48/stock/media/stock_xfburn-burn-cd.png
/usr/share/icons/hicolor/48x48/stock/media/stock_xfburn-data-copy.png
/usr/share/icons/hicolor/48x48/stock/media/stock_xfburn-import-session.png
/usr/share/icons/hicolor/48x48/stock/media/stock_xfburn-new-data-composition.png
/usr/share/icons/hicolor/48x48/stock/media/stock_xfburn.png
/usr/share/icons/hicolor/scalable/stock/media/stock_xfburn-audio-cd.svg
/usr/share/icons/hicolor/scalable/stock/media/stock_xfburn-blank-cdrw.svg
/usr/share/icons/hicolor/scalable/stock/media/stock_xfburn-burn-cd.svg
/usr/share/icons/hicolor/scalable/stock/media/stock_xfburn-data-copy.svg
/usr/share/icons/hicolor/scalable/stock/media/stock_xfburn-import-session.svg
/usr/share/icons/hicolor/scalable/stock/media/stock_xfburn-new-data-composition.svg
/usr/share/icons/hicolor/scalable/stock/media/stock_xfburn.svg
/usr/share/xfburn/xfburn-toolbars.ui
/usr/share/xfburn/xfburn.ui

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfburn/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfburn.1

%files locales -f xfburn.lang
%defattr(-,root,root,-)

