%define major 5
%define libname %mklibname KF5KMahjongglib %{major}
%define devname %mklibname KF5KMahjongglib -d

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		libkmahjongg
Summary:	Library used for loading and rendering of Mahjongg tilesets
Version:	17.03.80
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)

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

%files -n kmahjongglib
%{_datadir}/kmahjongglib

#-------------------------------------------------------------------------------

%package -n %{libname}
Summary:	Runtime library for KMahjongg
Group:		System/Libraries
Requires:	kmahjongglib = %{EVRD}
Obsoletes:	%{mklibname kf5kmahjongglib 5} < 1:15.12.0

%description -n %{libname}
Runtime library for KMahjongg.

%files -n %{libname}
%{_libdir}/libKF5KMahjongglib.so.%{major}*

#-------------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers files for KMahjongg library
Group:		Development/KDE and Qt
Conflicts:	kdegames4-devel < 1:4.9.80
Requires:	cmake(KF5KDEGames)
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{mklibname kf5kmahjongglib -d} < 1:15.12.0
%rename %{name}-devel

%description -n %{devname}
Headers files needed to build applications based on KMahjongg library.

%files -n %{devname}
%{_libdir}/libKF5KMahjongglib.so
%{_libdir}/cmake/KF5KMahjongglib
%{_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
