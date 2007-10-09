%define name cdecl
%define version 2.5
%define release %mkrel 23


Summary: Programs for encoding and decoding C and C++ function declarations
Name: %name
Version: %version
Release: %release
License: Distributable
Group: Development/C
Source: %{name}-%{version}.tar.bz2
Url: ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/
Patch: cdecl-2.5.misc_conflicts.patch
BuildRequires: readline-devel
BuildRequires: libtermcap-devel
BuildRequires: byacc
BuildRequires: flex
BuildRoot: %{_tmppath}/%{name}-root

%description
The cdecl package includes the cdecl and c++decl utilities, which are
used to translate English to C or C++ function declarations and vice
versa.

You should install the cdecl package if you intend to do C and/or C++
programming.

%prep

%setup -q

%patch -p1

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

