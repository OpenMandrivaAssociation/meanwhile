%define name   meanwhile 
%define version 1.0.2
%define release %mkrel 1
%define Summary  Lotus Sametime Community Client library

%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}

# Hack :-(
%define __libtoolize /bin/true

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release

License:	LGPL
Group:		System/Libraries
URL:		http://meanwhile.sourceforge.net/

Source: 	http://kent.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	glib2-devel >= 2.2
BuildRequires:	doxygen

%description
The heart of the Meanwhile Project is the Meanwhile library, providing the
basic Lotus Sametime session functionality along with the core services;
Presence, Messaging, Conferencing, and Storage. This extensible client
interface allows additional services to be added to a session at runtime,
allowing for simple integration of future service handlers such as
whiteboard, screen-sharing, and file transfer.

%package -n %{lib_name}
Summary: Library used for Lotus Sametime connectivity
Group: Development/C
Provides: %{name} = %{version}-%{release}

%description -n %{lib_name}
The heart of the Meanwhile Project is the Meanwhile library, providing the
basic Lotus Sametime session functionality along with the core services;
Presence, Messaging, Conferencing, and Storage. This extensible client
interface allows additional services to be added to a session at runtime,
allowing for simple integration of future service handlers such as
whiteboard, screen-sharing, and file transfer.

%package -n %{lib_name}-devel
Summary: Header files and libraries for %{name}
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{lib_name_orig}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{lib_name}-devel
This package contains the header files and static libraries for %{name}.
If you would like to develop programs using %{name}, you will need to
install %{name}-devel.

%package -n %{lib_name}-doc
Summary: Documentation for the %{name} library
Group: Development/C

%description -n %{lib_name}-doc
Documentation for the %{name} library. 

%prep
%setup

%build
%configure
%make

%install
rm -rf %buildroot
%makeinstall

%clean
rm -rf %buildroot

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_libdir}/libmeanwhile.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%{_includedir}/meanwhile
%{_libdir}/libmeanwhile.a
%{_libdir}/libmeanwhile.la
%{_libdir}/libmeanwhile.so
%{_libdir}/pkgconfig/meanwhile.pc

%files -n %{lib_name}-doc
%defattr(-,root,root)
%{_datadir}/doc/%{name}-doc-%{version}/


