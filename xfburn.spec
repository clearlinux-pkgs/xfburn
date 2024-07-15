#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v16
# autospec commit: b858a2a
#
Name     : xfburn
Version  : 0.7.1
Release  : 12
URL      : https://archive.xfce.org/src/apps/xfburn/0.7/xfburn-0.7.1.tar.bz2
Source0  : https://archive.xfce.org/src/apps/xfburn/0.7/xfburn-0.7.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfburn-bin = %{version}-%{release}
Requires: xfburn-data = %{version}-%{release}
Requires: xfburn-license = %{version}-%{release}
Requires: xfburn-locales = %{version}-%{release}
Requires: xfburn-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : exo-dev
BuildRequires : file
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(exo-2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gstreamer-pbutils-1.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libburn-1)
BuildRequires : pkgconfig(libisofs-1)
BuildRequires : pkgconfig(libxfce4ui-2)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
xfburn
======
Version 0.7.0, 2023-03-03
[xfburn's website](https://docs.xfce.org/apps/xfburn/start)

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
%setup -q -n xfburn-0.7.1
cd %{_builddir}/xfburn-0.7.1
pushd ..
cp -a xfburn-0.7.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721067230
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1721067230
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfburn
cp %{_builddir}/xfburn-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xfburn/4cc77b90af91e615a64ae04893fdffa7939db84c || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang xfburn
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xfburn
/usr/bin/xfburn

%files data
%defattr(-,root,root,-)
/usr/share/Thunar/sendto/thunar-sendto-xfburn.desktop
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
/usr/share/metainfo/org.xfce.xfburn.appdata.xml
/usr/share/xfburn/xfburn-popup-menus.ui
/usr/share/xfburn/xfburn-toolbars.ui
/usr/share/xfburn/xfburn.ui

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfburn/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfburn.1

%files locales -f xfburn.lang
%defattr(-,root,root,-)

