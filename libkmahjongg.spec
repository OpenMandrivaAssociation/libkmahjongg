%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		libkmahjongg
Summary:	Library used for loading and rendering of Mahjongg tilesets
Version:	14.12.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:14.11.97-1
- New version 14.11.97

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

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

