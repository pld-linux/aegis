Summary:	Project change supervisor
Name:		aegis
Version:	3.12
Release:	2
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz±dzanie wersjami
Copyright:	GPL
URL:		http://www.canb.auug.org.au/~millerp/aegis.html
#Icon:		aegis.gif
Source:		http://www.canb.auug.org.au/~millerp/aegis-3.12.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Aegis is a transaction-based software configuration management system.
It provides a framework within which a team of developers may work
on many changes to a program independently, and Aegis coordinates
integrating these changes back into the master source of the program,
with as little disruption as possible.

#%package txtdocs
#Summary: Aegis documentation, dumb ascii text
#Group: Development/Building

#%description txtdocs
#Aegis documentation in dumb ascii text format.

#%package psdocs
#Summary: Aegis documentation, PostScript format
#Group: Development/Building

#%description psdocs
#Aegis documentation in PostScript format.

#%package dvidocs
#Summary: aegis documentation, DVI format
#Group: Development/Building

#%description dvidocs
#Aegis documentation in DVI format.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s
./configure %{_target_platform} \
	--prefix=/usr
make

%install
make install RPM_BUILD_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%dir /usr/com/aegis
%dir %{_libdir}/aegis
%dir %{_datadir}/aegis

%attr(0755,root,root) %{_bindir}/aedist
%attr(0755,root,root) %{_bindir}/aefind
%attr(4755,root,root) %{_bindir}/aegis
%attr(0755,root,root) %{_bindir}/aerect
%attr(0755,root,root) %{_bindir}/aereport

%attr(0755,root,root) /home/httpd/cgi-bin/aegis.cgi
%attr(0755,root,root) %{_datadir}/aegis/db_forced.sh
%attr(0755,root,root) %{_datadir}/aegis/de.inews.sh
%attr(0755,root,root) %{_datadir}/aegis/de.sh
%attr(0755,root,root) %{_datadir}/aegis/deu.inews.sh
%attr(0755,root,root) %{_datadir}/aegis/deu.sh
%attr(0755,root,root) %{_datadir}/aegis/if.inews.sh
%attr(0755,root,root) %{_datadir}/aegis/if.sh
%attr(0755,root,root) %{_datadir}/aegis/integrate_q.sh
%attr(0755,root,root) %{_datadir}/aegis/ip.inews.sh
%attr(0755,root,root) %{_datadir}/aegis/ip.sh
%attr(0755,root,root) %{_datadir}/aegis/remind/awt_dvlp.sh
%attr(0755,root,root) %{_datadir}/aegis/remind/awt_intgrtn.sh
%attr(0755,root,root) %{_datadir}/aegis/remind/bng_dvlpd.sh
%attr(0755,root,root) %{_datadir}/aegis/remind/bng_rvwd.sh
%attr(0755,root,root) %{_datadir}/aegis/rf.inews.sh
%attr(0755,root,root) %{_datadir}/aegis/rf.sh
%attr(0755,root,root) %{_datadir}/aegis/rp.inews.sh
%attr(0755,root,root) %{_datadir}/aegis/rp.sh
%attr(0755,root,root) %{_datadir}/aegis/rpu.inews.sh
%attr(0755,root,root) %{_datadir}/aegis/rpu.sh

%{_datadir}/aegis/aegis.icon
%{_datadir}/aegis/aegis.mask
%{_datadir}/aegis/aegis.pgm
%{_datadir}/aegis/config.example/architecture
%{_datadir}/aegis/config.example/cake
%{_datadir}/aegis/config.example/cook
%{_datadir}/aegis/config.example/fhist
%{_datadir}/aegis/config.example/make
%{_datadir}/aegis/config.example/rcs
%{_datadir}/aegis/config.example/sccs
%{_datadir}/aegis/cshrc

%{_libdir}/aegis/en/LC_MESSAGES/*
%{_datadir}/aegis/en/html/*
%{_mandir}/man[15]/*

%{_datadir}/aegis/en/notes/locale.man
%{_datadir}/aegis/profile
%{_datadir}/aegis/report.index
%{_datadir}/aegis/report/*

#%files txtdocs
#%attr(0644,root,root) %{_datadir}/aegis/en/auug93.txt
#%attr(0644,root,root) %{_datadir}/aegis/en/auug96.txt
#%attr(0644,root,root) %{_datadir}/aegis/en/auug97.txt
#%attr(0644,root,root) %{_datadir}/aegis/en/faq.txt
#%attr(0644,root,root) %{_datadir}/aegis/en/refman.txt
#%attr(0644,root,root) %{_datadir}/aegis/en/user-guide.txt

#%files psdocs
#%attr(0644,root,root) %{_datadir}/aegis/en/auug93.ps
#%attr(0644,root,root) %{_datadir}/aegis/en/auug96.ps
#%attr(0644,root,root) %{_datadir}/aegis/en/auug97.ps
#%attr(0644,root,root) %{_datadir}/aegis/en/faq.ps
#%attr(0644,root,root) %{_datadir}/aegis/en/refman.ps
#%attr(0644,root,root) %{_datadir}/aegis/en/user-guide.ps

#%files dvidocs
#%attr(0644,root,root) %{_datadir}/aegis/en/auug93.dvi
#%attr(0644,root,root) %{_datadir}/aegis/en/auug96.dvi
#%attr(0644,root,root) %{_datadir}/aegis/en/auug97.dvi
#%attr(0644,root,root) %{_datadir}/aegis/en/faq.dvi
#%attr(0644,root,root) %{_datadir}/aegis/en/refman.dvi
#%attr(0644,root,root) %{_datadir}/aegis/en/user-guide.dvi
