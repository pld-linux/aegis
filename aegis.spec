Summary:	Project change supervisor
Summary(pl):	Nadzorca zmian w projektach
Name:		aegis
Version:	3.18
Release:	2
License:	GPL
Group:		Development/Version Control
Source0:	http://www.canb.auug.org.au/~millerp/aegis/%{name}-%{version}.tar.gz
Patch0:		%{name}-ugid.patch
Patch1:		%{name}-etc_dir.patch
Patch2:		%{name}-pmake.patch
URL:		http://www.canb.auug.org.au/~millerp/aegis.html
Icon:		aegis.gif
BuildRequires:	zlib-devel
Requires(pre):	user-aegis
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
%patch2 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/{aegis,locale},%{_libdir},%{_mandir}/man1}

%{__make} install \
	AEGIS_UID=`id -ru` \
	AEGIS_GID=`id -rg` \
	HAVE_WEB=yes ScriptRoot=/home/services/httpd/cgi-bin

mv -f $RPM_BUILD_ROOT%{_libdir}/aegis/en $RPM_BUILD_ROOT%{_datadir}/locale
rm -rf $RPM_BUILD_ROOT%{_datadir}/aegis/man1
rm -rf $RPM_BUILD_ROOT%{_datadir}/aegis/en
rm -f lib/en/html/.mkdir*

%clean
rm -rf $RPM_BUILD_ROOT

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
%attr(0755,root,root) %{_bindir}/tk*

%attr(0755,root,root) /home/services/httpd/cgi-bin/aegis.cgi
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
