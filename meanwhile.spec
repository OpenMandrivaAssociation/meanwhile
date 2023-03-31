%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Lotus Sametime Community Client library
Name:		meanwhile
Version:	1.1.1
Release:	3
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/obriencj/meanwhile
Source0:	https://github.com/obriencj/meanwhile/archive/v%{version}/%{name}-%{version}.tar.gz
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
%autosetup -p1

%build
%configure \
	--disable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libmeanwhile.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README TODO
%{_includedir}/meanwhile
%{_libdir}/libmeanwhile.so
%{_libdir}/pkgconfig/meanwhile.pc
%{_datadir}/doc/%{name}-doc-%{version}/
