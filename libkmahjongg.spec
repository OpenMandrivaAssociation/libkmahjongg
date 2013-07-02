Name:		libkmahjongg
Summary:	Library used for loading and rendering of Mahjongg tilesets
Version:	4.10.5
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

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
%{_kde_appsdir}/kmahjongglib

#-------------------------------------------------------------------------------

%define libkmahjongglib_major 4
%define libkmahjongglib %mklibname kmahjongglib %{libkmahjongglib_major}

%package -n %{libkmahjongglib}
Summary:	Runtime library for KMahjongg
Group:		System/Libraries
Requires:	kmahjongglib

%description -n %{libkmahjongglib}
Runtime library for KMahjongg.

%files -n %{libkmahjongglib}
%{_kde_libdir}/libkmahjongglib.so.%{libkmahjongglib_major}*

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
%{_kde_libdir}/libkmahjongglib.so
%{_kde_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

