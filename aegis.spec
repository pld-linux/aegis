Summary:	Project change supervisor
Name:		aegis
Version:	3.18
Release:	1
License:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Zarządzanie wersjami
Source0:	http://www.canb.auug.org.au/~millerp/aegis/%{name}-%{version}.tar.gz
Patch0:		aegis-ugid.patch
URL:		http://www.canb.auug.org.au/~millerp/aegis.html
Icon:		aegis.gif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aegis is a transaction-based software configuration management system.
It provides a framework within which a team of developers may work on
many changes to a program independently, and Aegis coordinates
integrating these changes back into the master source of the program,
with as little disruption as possible.

%prep
%setup -q
%patch -p1

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/{aegis,locale},%{_libdir},%{_mandir}/man1}

%{__make} install \
	AEGIS_UID=`id -ru` \
	AEGIS_GID=`id -rg`

mv -f $RPM_BUILD_ROOT%{_libdir}/aegis/en $RPM_BUILD_ROOT%{_datadir}/locale
rm -rf $RPM_BUILD_ROOT%{_datadir}/aegis/man1
rm -rf $RPM_BUILD_ROOT%{_datadir}/aegis/en
rm -f lib/en/html/.mkdir*

gzip -9nf lib/en/{*.{txt,ps},notes/locale.man} README \
	$RPM_BUILD_ROOT%{_mandir}/man{1,5}/*

%pre
%{_sbindir}/groupadd -g 65 aegis
%{_sbindir}/useradd -u 65 -g 65 -c "Project change supervisor" aegis
%{_bindir}/update-db

%postun
if [ $1 = 0 ] ; then
	%{_sbindir}/userdel aegis
	%{_sbindir}/groupdel aegis
	%{_bindir}/update-db
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lib/en/*.{ps,txt}.gz lib/en/notes/locale.man.gz lib/en/html README.gz

%dir %attr(755,aegis,aegis) %{_prefix}/com/aegis
%dir %attr(755,aegis,aegis) %{_libdir}/aegis
%dir %{_datadir}/aegis

%attr(0755,root,root) %{_bindir}/aedist
%attr(0755,root,root) %{_bindir}/aefind
%attr(4755,root,root) %{_bindir}/aegis
%attr(0755,root,root) %{_bindir}/aerect
%attr(0755,root,root) %{_bindir}/aereport
%attr(0755,root,root) %{_bindir}/tk*

%attr(0755,root,root) /home/httpd/cgi-bin/aegis.cgi
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
