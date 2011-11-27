%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}
%define lib_devel %mklibname %{name} -d

Summary:        Lotus Sametime Community Client library
Name:           meanwhile
Version:        1.0.2
Release:        7

License:	LGPL
Group:		System/Libraries
URL:		http://meanwhile.sourceforge.net/

Source: 	http://kent.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		meanwhile-1.0.2-fix-str-fmt.patch
Patch1:		http://ie.archive.ubuntu.com/gentoo-portage/net-libs/meanwhile/files/meanwhile-1.0.2-presence.patch
Patch2:		meanwhile-crash.patch
Patch3:		meanwhile-fix-glib-headers.patch

BuildRequires:	glib2-devel >= 2.2
BuildRequires:	doxygen

%description
The heart of the Meanwhile Project is the Meanwhile library, providing the
basic Lotus Sametime session functionality along with the core services;
Presence, Messaging, Conferencing, and Storage. This extensible client
interface allows additional services to be added to a session at runtime,
allowing for simple integration of future service handlers such as
whiteboard, screen-sharing, and file transfer.

%package -n	%{lib_name}
Summary:	Library used for Lotus Sametime connectivity
Group:		Development/C
Provides:	%{name} = %{version}-%{release}

%description -n %{lib_name}
The heart of the Meanwhile Project is the Meanwhile library, providing the
basic Lotus Sametime session functionality along with the core services;
Presence, Messaging, Conferencing, and Storage. This extensible client
interface allows additional services to be added to a session at runtime,
allowing for simple integration of future service handlers such as
whiteboard, screen-sharing, and file transfer.

%package -n	%{lib_devel}
Summary:	Header files and libraries for %{name}
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
%rename		%{_lib}%{name}1-devel

%description -n	%{lib_devel}
This package contains the header files and static libraries for %{name}.
If you would like to develop programs using %{name}, you will need to
install %{name}-devel.

%package -n	%{name}-doc
Summary:	Documentation for the %{name} library
Group:		Development/C
%rename		%{_lib}%{name}1-doc

%description -n	%{name}-doc
Documentation for the %{name} library. 

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0 -b .crash~
%patch3 -p1 -b .glib~

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{lib_name}
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_libdir}/libmeanwhile.so.%{lib_major}*

%files -n %{lib_devel}
%{_includedir}/meanwhile
%{_libdir}/libmeanwhile.a
%{_libdir}/libmeanwhile.la
%{_libdir}/libmeanwhile.so
%{_libdir}/pkgconfig/meanwhile.pc

%files -n %{name}-doc
%{_datadir}/doc/%{name}-doc-%{version}/
