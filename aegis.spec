#
# TODO:
#	- check %%files for missing items
#
Summary:	Project change supervisor
Summary(pl):	Nadzorca zmian w projektach
Name:		aegis
Version:	4.16
Release:	2
License:	GPL
Group:		Development/Version Control
Source0:	http://dl.sourceforge.net/aegis/%{name}-%{version}.tar.gz
# Source0-md5:	134d01cca1e7173d4396884df5b669eb
Patch0:		%{name}-ugid.patch
Patch1:		%{name}-etc_dir.patch
URL:		http://aegis.sourceforge.net/
Icon:		aegis.gif
BuildRequires:	bison
BuildRequires:	zlib-devel
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sharedstatedir		/var/lib

%description
Aegis is a transaction-based software configuration management system.
It provides a framework within which a team of developers may work on
many changes to a program independently, and Aegis coordinates
integrating these changes back into the master source of the program,
with as little disruption as possible.

%description -l pl
Aegis jest transakcyjnie dzia³aj±cym programem do zarz±dzania
konfiguracj±. Daje ¶rodowisko w którym za³oga developerów mo¿e
pracowaæ nad wieloma zmianami w programie niezale¿nie, a Aegis
koordynuje integracjê tych zmian w g³ówne ¼ród³a programu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/{aegis,locale},%{_libdir},%{_mandir}/man1}

%{__make} install \
	AEGIS_UID=`id -ru` \
	AEGIS_GID=`id -rg` \
	HAVE_WEB=yes ScriptRoot=/srv/httpd/cgi-bin

mv -f $RPM_BUILD_ROOT%{_libdir}/aegis/en $RPM_BUILD_ROOT%{_datadir}/locale
rm -rf $RPM_BUILD_ROOT%{_datadir}/aegis/man1
rm -rf $RPM_BUILD_ROOT%{_datadir}/aegis/en
rm -f lib/en/html/.mkdir*

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`/usr/bin/getgid aegis`" ]; then
	if [ "`/usr/bin/getgid aegis`" != "65" ]; then
		echo "Error: group aegis doesn't have gid=65. Correct this before installing aegis." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 65 aegis
fi
if [ -n "`/bin/id -u aegis 2>/dev/null`" ]; then
	if [ "`/bin/id -u aegis`" != "65" ]; then
		echo "Error: user aegis doesn't have uid=65. Correct this before installing aegis." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 65 -g 65 -c "Project change supervisor" aegis 1>&2
fi

%postun
if [ "$1" = "0" ] ; then
	/usr/sbin/userdel aegis 2>/dev/null
	/usr/sbin/groupdel aegis 2>/dev/null
fi

%files
%defattr(644,root,root,755)
%doc lib/en/*.{ps,txt} lib/en/notes/locale.man lib/en/html README

%dir %attr(775,root,aegis) %{_sharedstatedir}/aegis
%dir %attr(755,root,aegis) %{_libdir}/aegis
%dir %{_datadir}/aegis

%attr(0755,root,root) %{_bindir}/aedist
%attr(0755,root,root) %{_bindir}/aefind
%attr(4755,root,root) %{_bindir}/aegis
%attr(0755,root,root) %{_bindir}/aerect
%attr(0755,root,root) %{_bindir}/aereport
%attr(0755,root,root) %{_bindir}/ae-sccs-put
%attr(0755,root,root) %{_bindir}/ae_diff2htm
%attr(0755,root,root) %{_bindir}/aeannotate
%attr(0755,root,root) %{_bindir}/aebuffy
%attr(0755,root,root) %{_bindir}/aecomp
%attr(0755,root,root) %{_bindir}/aecomplete
%attr(0755,root,root) %{_bindir}/aeimport
%attr(0755,root,root) %{_bindir}/aeintegratq
%attr(0755,root,root) %{_bindir}/aels
%attr(0755,root,root) %{_bindir}/aemeasure
%attr(0755,root,root) %{_bindir}/aepatch
%attr(0755,root,root) %{_bindir}/aesub
%attr(0755,root,root) %{_bindir}/aetar
%attr(0755,root,root) %{_bindir}/xaegis
%attr(0755,root,root) %{_bindir}/aegis.cgi
%attr(0755,root,root) %{_bindir}/tk*
%attr(0755,root,root) %{_datadir}/aegis/*.sh
%attr(0755,root,root) %{_datadir}/aegis/remind/*

%{_datadir}/aegis/aegis.icon
%{_datadir}/aegis/aegis.mask
%{_datadir}/aegis/aegis.pgm
%{_datadir}/aegis/cshrc
%{_datadir}/aegis/profile
%{_datadir}/aegis/report.index
%{_datadir}/aegis/config.example/*
%{_datadir}/aegis/report/*
%{_datadir}/aegis/wish/*
%{_mandir}/man[15]/*
