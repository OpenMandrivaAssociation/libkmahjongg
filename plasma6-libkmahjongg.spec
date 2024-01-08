%define major 6
%define libname %mklibname KMahjongg6 %{major}
%define devname %mklibname KMahjongg6 -d

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-libkmahjongg
Summary:	Library used for loading and rendering of Mahjongg tilesets
Version:	24.01.85
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libkmahjongg-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)

%description
This package provides the library for loading and rendering of Mahjongg
tilesets and associated backgrounds, used by KMahjongg, Kajongg and KShisen.

#------------------------------------------------------------------------------

%package -n kmahjongglib
Summary:	Common files needed by KMahjongg, Kajongg and KShisen
Group:		Games/Other
BuildArch:	noarch

%description -n kmahjongglib
Common files needed by KMahjongg, Kajongg and KShisen.

%files -n kmahjongglib -f libkmahjongg6.lang
%{_datadir}/qlogging-categories6/libkmahjongg.categories
%{_datadir}/kmahjongglib

#-------------------------------------------------------------------------------

%package -n %{libname}
Summary:	Runtime library for KMahjongg
Group:		System/Libraries
Requires:	kmahjongglib = %{EVRD}

%description -n %{libname}
Runtime library for KMahjongg.

%files -n %{libname}
%{_libdir}/libKMahjongg6.so.%{major}*

#-------------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers files for KMahjongg library
Group:		Development/KDE and Qt
Requires:	cmake(KF6KDEGames)
Requires:	%{libname} = %{EVRD}
%rename %{name}-devel

%description -n %{devname}
Headers files needed to build applications based on KMahjongg library.

%files -n %{devname}
%{_libdir}/libKMahjongg6.so
%{_libdir}/cmake/KMahjongglib6
%{_includedir}/*

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n libkmahjongg-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkmahjongg6
