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
./configure \
	--prefix=/usr
make

%install
make RPM_BUILD_ROOT=$RPM_BUILD_ROOT install

%post
chown -R 3 /usr/com/aegis /usr/lib/aegis /usr/share/aegis
chgrp -R 3 /usr/com/aegis /usr/lib/aegis /usr/share/aegis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%dir /usr/com/aegis
%dir /usr/lib/aegis
%dir /usr/share/aegis

%attr(0755,root,root) /usr/bin/aedist
%attr(0755,root,root) /usr/bin/aefind
%attr(4755,root,root) /usr/bin/aegis
%attr(0755,root,root) /usr/bin/aerect
%attr(0755,root,root) /usr/bin/aereport

%attr(0755,root,root) /home/httpd/cgi-bin/aegis.cgi
%attr(0755,root,root) /usr/share/aegis/db_forced.sh
%attr(0755,root,root) /usr/share/aegis/de.inews.sh
%attr(0755,root,root) /usr/share/aegis/de.sh
%attr(0755,root,root) /usr/share/aegis/deu.inews.sh
%attr(0755,root,root) /usr/share/aegis/deu.sh
%attr(0755,root,root) /usr/share/aegis/if.inews.sh
%attr(0755,root,root) /usr/share/aegis/if.sh
%attr(0755,root,root) /usr/share/aegis/integrate_q.sh
%attr(0755,root,root) /usr/share/aegis/ip.inews.sh
%attr(0755,root,root) /usr/share/aegis/ip.sh
%attr(0755,root,root) /usr/share/aegis/remind/awt_dvlp.sh
%attr(0755,root,root) /usr/share/aegis/remind/awt_intgrtn.sh
%attr(0755,root,root) /usr/share/aegis/remind/bng_dvlpd.sh
%attr(0755,root,root) /usr/share/aegis/remind/bng_rvwd.sh
%attr(0755,root,root) /usr/share/aegis/rf.inews.sh
%attr(0755,root,root) /usr/share/aegis/rf.sh
%attr(0755,root,root) /usr/share/aegis/rp.inews.sh
%attr(0755,root,root) /usr/share/aegis/rp.sh
%attr(0755,root,root) /usr/share/aegis/rpu.inews.sh
%attr(0755,root,root) /usr/share/aegis/rpu.sh

/usr/share/aegis/aegis.icon
/usr/share/aegis/aegis.mask
/usr/share/aegis/aegis.pgm
/usr/share/aegis/config.example/architecture
/usr/share/aegis/config.example/cake
/usr/share/aegis/config.example/cook
/usr/share/aegis/config.example/fhist
/usr/share/aegis/config.example/make
/usr/share/aegis/config.example/rcs
/usr/share/aegis/config.example/sccs
/usr/share/aegis/cshrc

/usr/lib/aegis/en/LC_MESSAGES/*
/usr/share/aegis/en/html/*
/usr/man/man[15]/*

/usr/share/aegis/en/notes/locale.man
/usr/share/aegis/profile
/usr/share/aegis/report.index
/usr/share/aegis/report/*

#%files txtdocs
#%attr(0644,root,root) /usr/share/aegis/en/auug93.txt
#%attr(0644,root,root) /usr/share/aegis/en/auug96.txt
#%attr(0644,root,root) /usr/share/aegis/en/auug97.txt
#%attr(0644,root,root) /usr/share/aegis/en/faq.txt
#%attr(0644,root,root) /usr/share/aegis/en/refman.txt
#%attr(0644,root,root) /usr/share/aegis/en/user-guide.txt

#%files psdocs
#%attr(0644,root,root) /usr/share/aegis/en/auug93.ps
#%attr(0644,root,root) /usr/share/aegis/en/auug96.ps
#%attr(0644,root,root) /usr/share/aegis/en/auug97.ps
#%attr(0644,root,root) /usr/share/aegis/en/faq.ps
#%attr(0644,root,root) /usr/share/aegis/en/refman.ps
#%attr(0644,root,root) /usr/share/aegis/en/user-guide.ps

#%files dvidocs
#%attr(0644,root,root) /usr/share/aegis/en/auug93.dvi
#%attr(0644,root,root) /usr/share/aegis/en/auug96.dvi
#%attr(0644,root,root) /usr/share/aegis/en/auug97.dvi
#%attr(0644,root,root) /usr/share/aegis/en/faq.dvi
#%attr(0644,root,root) /usr/share/aegis/en/refman.dvi
#%attr(0644,root,root) /usr/share/aegis/en/user-guide.dvi

%changelog
* Fri Apr  2 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [3.12-2]
  (based on spec by anonymous)
- added Group(pl)
- sloted BuildRoot into PLD standard
- added %changelog
- added %defattr(644,root,root,755)
- simplifications in %files
- root instead bin group on files
- added -q %setup parameter
- commented Icon (not available)
