%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		libkmahjongg
Summary:	Library used for loading and rendering of Mahjongg tilesets
Version:	15.04.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)

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

%package devel
Summary:	Headers files for KMahjongg library
Group:		Development/KDE and Qt
Conflicts:	kdegames4-devel < 1:4.9.80
Requires:	libkdegames-devel
Requires:	%{libkmahjongglib} = %{EVRD}

%description devel
Headers files needed to build applications based on KMahjongg library.

%files devel
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
