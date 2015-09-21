%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		libkmahjongg
Summary:	Library used for loading and rendering of Mahjongg tilesets
Version:	15.08.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
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

%define libkmahjongglib_major 5
%define libkmahjongglib %mklibname kf5kmahjongglib %{libkmahjongglib_major}

%package -n %{libkmahjongglib}
Summary:	Runtime library for KMahjongg
Group:		System/Libraries
Requires:	kmahjongglib
Obsoletes:	%{mklibname kmahjongglib 4} < %{EVRD}

%description -n %{libkmahjongglib}
Runtime library for KMahjongg.

%files -n %{libkmahjongglib}
%{_libdir}/libKF5KMahjongglib.so.%{libkmahjongglib_major}*

#-------------------------------------------------------------------------------

%define devname %mklibname kf5mahjongglib -d
%package -n %{devname}
Summary:	Headers files for KMahjongg library
Group:		Development/KDE and Qt
Conflicts:	kdegames4-devel < 1:4.9.80
Requires:	libkdegames-devel
Requires:	%{libkmahjongglib} = %{EVRD}
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
