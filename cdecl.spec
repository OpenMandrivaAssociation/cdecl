Summary:	Programs for encoding and decoding C and C++ function declarations
Name:		cdecl
Version:	2.5
Release:	30
License:	Distributable
Group:		Development/C
Source0:	%{name}-%{version}.tar.bz2
Url:		ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/
Patch1:		cdecl-2.5-fix-conflicts.patch
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	readline-devel
BuildRequires:	termcap-devel

%description
The cdecl package includes the cdecl and c++decl utilities, which are
used to translate English to C or C++ function declarations and vice
versa.

You should install the cdecl package if you intend to do C and/or C++
programming.

%files
%{_bindir}/cdecl
%{_bindir}/c++decl
%{_mandir}/man1/cdecl.*
%{_mandir}/man1/c++decl.*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p0

%build
%make CFLAGS="%{optflags} -DUSE_READLINE"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall \
	BINDIR=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir}/man1/


