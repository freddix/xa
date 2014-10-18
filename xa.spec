Summary:	Cross-assembler for 6502 microprocessor
Name:		xa
Version:	2.3.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.floodgap.com/retrotech/xa/dists/%{name}-%{version}.tar.gz
# Source0-md5:	6e7ee302fc4cd8de3bf7f07abb336aca
URL:		http://www.floodgap.com/retrotech/xa/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
apg generates several random passwords. It uses several password
generation algorithms (currently two) and a built-in pseudo random
number generator.

%prep
%setup  -q

%build
%{__make} \
	CC="%{__cc}"	\
	CFLAGS="%{rpmldflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
    DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.1st TODO
%attr(755,root,root) %{_bindir}/file65
%attr(755,root,root) %{_bindir}/ldo65
%attr(755,root,root) %{_bindir}/printcbm
%attr(755,root,root) %{_bindir}/reloc65
%attr(755,root,root) %{_bindir}/uncpk
%attr(755,root,root) %{_bindir}/xa
%{_mandir}/man1/file65.1*
%{_mandir}/man1/ldo65.1*
%{_mandir}/man1/printcbm.1*
%{_mandir}/man1/reloc65.1*
%{_mandir}/man1/uncpk.1*
%{_mandir}/man1/xa.1*

