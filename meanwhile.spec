%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}
%define lib_devel %mklibname %{name} -d

Summary:	Lotus Sametime Community Client library
Name:		meanwhile
Version:	1.0.2
Release:	9
License:	LGPLv2+
Group:		System/Libraries
URL:		http://meanwhile.sourceforge.net/
Source0: 	http://kent.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		meanwhile-1.0.2-fix-str-fmt.patch
Patch1:		http://ie.archive.ubuntu.com/gentoo-portage/net-libs/meanwhile/files/meanwhile-1.0.2-presence.patch
Patch2:		meanwhile-crash.patch
Patch3:		meanwhile-fix-glib-headers.patch

BuildRequires:	pkgconfig(glib-2.0)
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
Requires:	%{lib_name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
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
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{lib_name}
%doc AUTHORS ChangeLog README TODO
%{_libdir}/libmeanwhile.so.%{lib_major}*

%files -n %{lib_devel}
%{_includedir}/meanwhile
%{_libdir}/libmeanwhile.so
%{_libdir}/pkgconfig/meanwhile.pc

%files -n %{name}-doc
%{_datadir}/doc/%{name}-doc-%{version}/

%changelog
* Mon Dec 12 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.2-8
+ Revision: 740315
- dup patch oops
- added p4 for glib 2.31 headers
- disabled static build

* Sun Nov 27 2011 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1.0.2-7
+ Revision: 734320
- drop useless 'INSTALL' file from docs
- drop COPYING from docs as it's provided by 'common-licenses'
- specify LGPL version in license
- use %%{EVRD} macro
- use %%rename macro
- drop bogus provides
- clean up package
- Fix glib.h build issues (rhbz#750023, P3 from Fedora)
- Add patch to fix crash when server removes contact list (P2 from Fedora

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6
+ Revision: 666410
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdv2011.0
+ Revision: 606635
- rebuild

* Fri Jan 15 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.2-4mdv2010.1
+ Revision: 491835
- apply libraries policy
- add patch to fix presence bug with recent sametime servers

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-3mdv2010.0
+ Revision: 426083
- rebuild

* Fri Apr 10 2009 Funda Wang <fwang@mandriva.org> 1.0.2-2mdv2009.1
+ Revision: 365830
- fix str fmt

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2009.0
+ Revision: 223228
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2008.1
+ Revision: 129837
- kill re-definition of %%buildroot on Pixel's request


* Fri Feb 16 2007 Nicholas Brown <nickbrown@mandriva.org> 1.0.2-1mdv2007.0
+ Revision: 121706
- Import meanwhile

* Tue Jan 31 2006 Jerome Soyer <saispo@mandriva.org> 1.0.2-1mdk
- New release 1.0.2

* Thu Dec 15 2005 Nick Brown <nickbrown@mandriva.org> 1.0.0-2mdk
- Fix library version number

* Thu Dec 15 2005 Nick Brown <nickbrown@mandriva.org> 1.0.0-1mdk
- 1.0.0

* Tue Nov 22 2005 Nick Brown <nickbrown@mandriva.org> 0.5.0-1mdk
- 0.5.0
- Add doc sub package

* Fri Jun 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.2-1mdk
- 0.4.2
- %%mkrel 
- Make Rpmbuildupdate happy

* Wed May 11 2005 Nick Brown <nickbrown@mandriva.org> 0.4.1-1mdk
- 0.4.1

* Tue Mar 22 2005 Nick Brown <nickbrown@mandrake.org> 0.4.0-1mdk
- 0.4.0

* Wed Mar 09 2005 Nick Brown <nickbrown@mandrake.org> 0.4.0-0.cvs20050309.1mdk
- cvs version of 0.4.0
- rpmlint, fix summary

* Thu Nov 11 2004 Nick Brown <nickbrown@mandrake.org> 0.3-2mdk
- Rebuild with re-released 0.3 (bug fixes).

* Sat Aug 07 2004 Nick Brown <nickbrown@mandrake.org> 0.3-1mdk
- First Mandrakelinux release.

