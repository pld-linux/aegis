# TODO: fix ScriptRoot
Summary:	Project change supervisor
Summary(pl.UTF-8):	Nadzorca zmian w projektach
Name:		aegis
Version:	4.16
Release:	4
License:	GPL
Group:		Development/Version Control
Source0:	http://dl.sourceforge.net/aegis/%{name}-%{version}.tar.gz
# Source0-md5:	134d01cca1e7173d4396884df5b669eb
Patch0:		%{name}-ugid.patch
Patch1:		%{name}-etc_dir.patch
URL:		http://aegis.sourceforge.net/
BuildRequires:	bison
BuildRequires:	curl-devel
BuildRequires:	libmagic-devel
BuildRequires:	rpmbuild(macros) >= 1.202
BuildRequires:	zlib-devel
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Provides:	group(aegis)
Provides:	user(aegis)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sharedstatedir		/var/lib

%description
Aegis is a transaction-based software configuration management system.
It provides a framework within which a team of developers may work on
many changes to a program independently, and Aegis coordinates
integrating these changes back into the master source of the program,
with as little disruption as possible.

%description -l pl.UTF-8
Aegis jest transakcyjnie działającym programem do zarządzania
konfiguracją. Daje środowisko w którym załoga developerów może
pracować nad wieloma zmianami w programie niezależnie, a Aegis
koordynuje integrację tych zmian w główne źródła programu.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/{aegis,locale},%{_libdir},%{_mandir}/man1}

%{__make} install \
	AEGIS_UID=`id -ru` \
	AEGIS_GID=`id -rg` \
	HAVE_WEB=yes \
	ScriptRoot=/srv/httpd/cgi-bin

mv -f $RPM_BUILD_ROOT%{_libdir}/aegis/en $RPM_BUILD_ROOT%{_datadir}/locale
rm -rf $RPM_BUILD_ROOT%{_datadir}/aegis/man1
rm -rf $RPM_BUILD_ROOT%{_datadir}/aegis/en
rm -f lib/en/html/.mkdir*

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 65 aegis
%useradd -u 65 -g 65 -c "Project change supervisor" aegis

%postun
if [ "$1" = "0" ] ; then
	%userremove aegis
	%groupremove aegis
fi

%files
%defattr(644,root,root,755)
%doc lib/en/*.{ps,txt} lib/en/notes/locale.man lib/en/html README

%dir %attr(775,root,aegis) %{_sharedstatedir}/aegis
%dir %attr(755,root,aegis) %{_libdir}/aegis
%dir %{_datadir}/aegis

%attr(755,root,root) %{_bindir}/aedist
%attr(755,root,root) %{_bindir}/aefind
%attr(4755,root,root) %{_bindir}/aegis
%attr(755,root,root) %{_bindir}/aerect
%attr(755,root,root) %{_bindir}/aereport
%attr(755,root,root) %{_bindir}/ae-sccs-put
%attr(755,root,root) %{_bindir}/ae_diff2htm
%attr(755,root,root) %{_bindir}/aeannotate
%attr(755,root,root) %{_bindir}/aebuffy
%attr(755,root,root) %{_bindir}/aecomp
%attr(755,root,root) %{_bindir}/aecomplete
%attr(755,root,root) %{_bindir}/aeimport
%attr(755,root,root) %{_bindir}/aeintegratq
%attr(755,root,root) %{_bindir}/aels
%attr(755,root,root) %{_bindir}/aemeasure
%attr(755,root,root) %{_bindir}/aepatch
%attr(755,root,root) %{_bindir}/aesub
%attr(755,root,root) %{_bindir}/aetar
%attr(755,root,root) %{_bindir}/xaegis
%attr(755,root,root) %{_bindir}/aegis.cgi
%attr(755,root,root) %{_bindir}/tk*
%attr(755,root,root) %{_datadir}/aegis/*.sh
%attr(755,root,root) %{_datadir}/aegis/remind

%{_datadir}/aegis/aegis.icon
%{_datadir}/aegis/aegis.mask
%{_datadir}/aegis/aegis.pgm
%{_datadir}/aegis/cshrc
%{_datadir}/aegis/profile
%{_datadir}/aegis/report.index
%{_datadir}/aegis/config.example
%{_datadir}/aegis/report
%{_datadir}/aegis/wish
%{_mandir}/man[15]/*
