Summary: Programs for encoding and decoding C and C++ function declarations
Name: cdecl
Version: 2.5
Release: 29
License: Distributable
Group: Development/C
Source: %{name}-%{version}.tar.bz2
Url: ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/
Patch1: cdecl-2.5-fix-conflicts.patch
BuildRequires: readline-devel
BuildRequires: termcap-devel
BuildRequires: byacc
BuildRequires: flex

%description
The cdecl package includes the cdecl and c++decl utilities, which are
used to translate English to C or C++ function declarations and vice
versa.

You should install the cdecl package if you intend to do C and/or C++
programming.

%prep
%setup -q
%patch1 -p0

%build

%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
%makeinstall \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/cdecl
%{_bindir}/c++decl
%{_mandir}/man1/cdecl.*
%{_mandir}/man1/c++decl.*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5-28mdv2011.0
+ Revision: 610114
- rebuild

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 2.5-27mdv2010.1
+ Revision: 541188
- fix conflicts on getline

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Mar 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.5-26mdv2009.1
+ Revision: 349389
- rebuild for latest readline

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.5-25mdv2009.0
+ Revision: 243465
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.5-23mdv2008.1
+ Revision: 136289
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot
    - fix man pages


* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 09:30:16 (55898)
- mkrelisation

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 09:22:47 (55896)
Import cdecl

* Sun Apr 03 2005 Michael Scherer <misc@mandrake.org> 2.5-22mdk
- Rebuild for readline

* Sun Nov 30 2003 Franck Villaume <fvill@freesurf.fr> 2.5-21mdk
- add BuildRequires flex

* Thu Nov 27 2003 Franck Villaume <fvill@freesurf.fr> 2.5-20mdk
- add BuildRequires byacc

