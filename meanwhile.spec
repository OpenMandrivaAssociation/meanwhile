%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Lotus Sametime Community Client library
Name:		meanwhile
Version:	1.0.2
Release:	10
License:	LGPLv2+
Group:		System/Libraries
Url:		http://meanwhile.sourceforge.net/
Source0: 	http://kent.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		meanwhile-1.0.2-fix-str-fmt.patch
Patch1:		http://ie.archive.ubuntu.com/gentoo-portage/net-libs/meanwhile/files/meanwhile-1.0.2-presence.patch
Patch2:		meanwhile-crash.patch
Patch3:		meanwhile-fix-glib-headers.patch
BuildRequires:	doxygen
BuildRequires:	pkgconfig(glib-2.0)

%description
The heart of the Meanwhile Project is the Meanwhile library, providing the
basic Lotus Sametime session functionality along with the core services;
Presence, Messaging, Conferencing, and Storage. This extensible client
interface allows additional services to be added to a session at runtime,
allowing for simple integration of future service handlers such as
whiteboard, screen-sharing, and file transfer.

%package -n	%{libname}
Summary:	Library used for Lotus Sametime connectivity
Group:		Development/C

%description -n %{libname}
The heart of the Meanwhile Project is the Meanwhile library, providing the
basic Lotus Sametime session functionality along with the core services;
Presence, Messaging, Conferencing, and Storage. This extensible client
interface allows additional services to be added to a session at runtime,
allowing for simple integration of future service handlers such as
whiteboard, screen-sharing, and file transfer.

%package -n	%{devname}
Summary:	Header files and libraries for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmeanwhile.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README TODO
%{_includedir}/meanwhile
%{_libdir}/libmeanwhile.so
%{_libdir}/pkgconfig/meanwhile.pc
%{_datadir}/doc/%{name}-doc-%{version}/

