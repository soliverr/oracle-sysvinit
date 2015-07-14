Summary   : Start/stop Oracle services.
Summary(ru_RU.UTF-8): Скрипты пуска/останова сервисов Oracle.
Name      : oracle-sysvinit
Version   : 1.4
Release   : 1
Group     : System Environment

Packager  : Kryazhevskikh Sergey, <soliverr@gmail.com>
License   : GPLv2

Requires  : initscripts
BuildArch : noarch

Source    : %{name}-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}

%define prefix          /
%define docdir          %_datadir/doc/%name-%version
%define sysconfdir      /etc
%define confdir         /etc/sysconfig
%define logdir          /var/log/oracle
%define liblsb          /lib/lsb
%define pkg_build_dir   %_builddir/%name-%version
%define pkg_functions   %pkg_build_dir/_pkg-functions

%package restart
Summary   : Start/stop Oracle Restart services.
Summary(ru_RU.UTF-8): Скрипты пуска/останова сервиса Oracle Restart.
Group     : oracle/base
Requires  : oracle-sysvinit

%package grid
Summary   : Start/stop Oracle Grid services.
Summary(ru_RU.UTF-8): Скрипты пуска/останова сервиса Oracle Grid.
Group     : oracle/base
Requires  : oracle-sysvinit

%package listener
Summary   : Start/stop Oracle Listener services.
Summary(ru_RU.UTF-8): Скрипты пуска/останова сервисов Oracle Listener.
Group     : oracle/base
Requires  : oracle-sysvinit

%package asm
Summary   : Start/stop Oracle ASM standalone RDBMS.
Summary(ru_RU.UTF-8): Скрипты пуска/останова автономного экземпляра СУБД Oracle ASM.
Group     : oracle/base
Requires  : oracle-sysvinit, oracle-sysvinit-restart

%package rdbms
Summary   : Start/stop Oracle RDBMS.
Summary(ru_RU.UTF-8): Скрипты пуска/останова СУБД Oracle.
Group     : oracle/base
Requires  : oracle-sysvinit

%package dbconsole
Summary   : Start/stop Oracle dbConsole service.
Summary(ru_RU.UTF-8): Скрипты пуска/останова сервиса dbConsole.
Group     : oracle/base
Requires  : oracle-sysvinit


%description
Control Oracle services in common Linux way through 
sysvinit.
.
This package contains common libraries to proper set up
Oracle environment variables.

%description -l ru_RU.UTF-8
Управление запуском/остановом сервисов Oracle типичным
для Linux способом с помощью sysvinit.
.
Данный пакет содержит общие библиотечные функции для установки
окружения для работы сервисов Oracle.


%description restart
Control Oracle Retsart services in common Linux way through 
sysvinit.
.
You should remove /etc/init.d/init.ohasd script to use scripts
from this package.

%description -l ru_RU.UTF-8 restart
Управление запуском/остановом сервисов Oracle типичным
для Linux способом с помощью sysvinit.
.
Вы должны удалить файл /etc/init.d/init.ohasd при использовании
скриптов пуска/останова данного пакета.


%description grid
Control Oracle Grid services in common Linux way through 
sysvinit.

%description -l ru_RU.UTF-8 grid
Управление запуском/остановом сервисов Oracle типичным
для Linux способом с помощью sysvinit.


%description listener
Control Oracle Listener services in common Linux way through
sysvinit.
.
This package intends to start standalone Oracle Listener services
configured through $TNS_ADMIN/listener.ora file.

%description -l ru_RU.UTF-8 listener
Управление запуском/остановом сервисов Oracle типичным
для Linux способом с помощью sysvinit.
.
Данный пакет предназначен для пуска/останова сервисов Oracle Listener,
сконфигурированных в файле $TNS_ADMIN/listener.ora.

%description asm
Control Oracle ASM standalone RDBMS in common Linux way through
sysvinit.
.
Use this package if ASM instance is not part of Oracle Restart or
Oracle Grid infrastructure.

%description -l ru_RU.UTF-8 asm
Управление запуском/остановом сервисов Oracle типичным
для Linux способом с помощью sysvinit.
.
Используйте данный пакет, если ASM экземпляр не является частью
Oracle Restart или Oracle Grid (Clusterware) инфраструктуры.

%description rdbms
Control Oracle RDBMS in common Linux way through sysvinit.
.
Use this package if Oracle RDBMS is not part of Oracle Restart or
Oracle Grid infrastructure and is not Oracle RAC instance.

%description -l ru_RU.UTF-8 rdbms
Управление запуском/остановом сервисов Oracle типичным
для Linux способом с помощью sysvinit.
.
Используйте данный пакет, если СУБД Oracle не является частью
Oracle Restart, Oracle Grid (Clusterware) инфраструктуры, а также
не является узлом Oracle Real Application Cluster.

%description dbconsole
Control Oracle dbConsole service in common Linux way through sysvinit.
.
Use this package if you use Oracle RDBMS version 10g or higher.

%description -l ru_RU.UTF-8 dbconsole
Управление запуском/остановом сервиса Oracle dbConsole типичным
для Linux способом с помощью sysvinit.
.
Используйте данный пакет, если вы используете СУБД Oracle версии
10g или выше.


%prep

%setup -q
./build.sh
./configure --prefix=%prefix --sysconfdir=%sysconfdir --docdir=%docdir \
  --with-liblsb=%liblsb --with-confdir=%confdir --with-logdir=%logdir

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{__make} install DESTDIR=$RPM_BUILD_ROOT/ DISTRIB=REDHAT

%pre
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=install
  version=
else
  action=upgrade
  version=`rpm -q %{name} --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
preinst "redhat" "$action" $version


%pre restart 
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=install
  version=
else
  action=upgrade
  version=`rpm -q %{name}-restart --queryformat '%{VERSION}-%{RELEASE}\n'`

fi
PACKAGE_NAME="%{name}-restart"
preinst "redhat" "$action" $version


%pre grid
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=install
  version=
else
  action=upgrade
  version=`rpm -q %{name}-grid --queryformat '%{VERSION}-%{RELEASE}\n'`

fi
PACKAGE_NAME="%{name}-grid"
preinst "redhat" "$action" $version


%pre listener
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=install
  version=
else
  action=upgrade
  version=`rpm -q %{name}-listener --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-listener"
preinst "redhat" "$action" $version


%pre asm
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=install
  version=
else
  action=upgrade
  version=`rpm -q %{name}-asm --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-asm"
preinst "redhat" "$action" $version


%pre rdbms
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=install
  version=
else
  action=upgrade
  version=`rpm -q %{name}-rdbms --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-rdbms"
preinst "redhat" "$action" $version


%pre dbconsole
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=install
  version=
else
  action=upgrade
  version=`rpm -q %{name}-dbconsole --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-dbconsole"
preinst "redhat" "$action" $version


%post
%include %pkg_functions
if [ $1 -eq 1 ] ; then
  action=configure
  version=
else
  action=upgrade
  version=`rpm -q %{name} --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
postinst "redhat" "$action" $version

%post restart 
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=configure
  version=
else
  action=upgrade
  version=`rpm -q %{name}-restart --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-restart"
postinst "redhat" "$action" $vesrion


%post grid
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=configure
  version=
else
  action=upgrade
  version=`rpm -q %{name}-grid --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-grid"
postinst "redhat" "$action" $version


%post listener
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=configure
  version=
else
  action=upgrade
  version=`rpm -q %{name}-listener --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-listener"
postinst "redhat" "$action" $version


%post asm
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=configure
  version=
else
  action=upgrade
  version=`rpm -q %{name}-asm --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-asm"
postinst "redhat" "$action" $version


%post rdbms
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=configure
  version=
else
  action=upgrade
  version=`rpm -q %{name}-rdbms --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-rdbms"
postinst "redhat" "$action" $version


%post dbconsole
%include %{pkg_functions}
if [ $1 -eq 1 ] ; then
  action=configure
  version=
else
  action=upgrade
  version=`rpm -q %{name}-dbconsole --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-dbconsole"
postinst "redhat" "$action" $version


%preun
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=remove
  version=
else
  action=upgrade
  version=`rpm -q %{name} --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
prerm "redhat" "$action" $version


%preun restart
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=remove
  version=
else
  action=upgrade
  version=`rpm -q %{name}-restart --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-restart"
prerm "redhat" "$action" $version


%preun grid
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=remove
  version=
else
  action=upgrade
  version=`rpm -q %{name}-grid --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-grid
prerm "redhat" "$action" $version


%preun listener
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=remove
  version=
else
  action=upgrade
  version=`rpm -q %{name}-listener --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-listener"
prerm "redhat" "$action" $version


%preun asm
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=remove
  version=
else
  action=upgrade
  version=`rpm -q %{name}-asm --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-asm"
prerm "redhat" "$action" $version


%preun rdbms
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=remove
  version=
else
  action=upgrade
  version=`rpm -q %{name}-rdbms --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-rdbms"
prerm "redhat" "$action" $version


%preun dbconsole
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=remove
  version=
else
  action=upgrade
  version=`rpm -q %{name}-dbconsole --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-dbconsole"
prerm "redhat" "$action" $version


%postun
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=purge
  version=
else
  action=upgrade
  version=`rpm -q %{name} --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
postrm "redhat" "$action" $version


%postun restart
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=purge
  version=
else
  action=upgrade
  version=`rpm -q %{name}-restart --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-restart"
postrm "redhat" "$action" $version


%postun grid
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=purge
  version=
else
  action=upgrade
  version=`rpm -q %{name}-grid --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-grid"
postrm "redhat" "$action" $version


%postun listener
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=purge
  version=
else
  action=upgrade
  version=`rpm -q %{name}-listener --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-listener"
postrm "redhat" "$action" $version


%postun asm
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=purge
  version=
else
  action=upgrade
  version=`rpm -q %{name}-asm --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-asm"
postrm "redhat" "$action" $version


%postun rdbms
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=purge
  version=
else
  action=upgrade
  version=`rpm -q %{name}-rdbms --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-rdbms"
postrm "redhat" "$action" $version


%postun dbconsole
%include %pkg_functions
if [ $1 -eq 0 ] ; then
  action=purge
  version=
else
  action=upgrade
  version=`rpm -q %{name}-dbconsole --queryformat '%{VERSION}-%{RELEASE}\n'`
fi
PACKAGE_NAME="%{name}-dbconsole"
postrm "redhat" "$action" $version


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
[ "%{pkg_build_dir}" != "/" ] && rm -rf %{pkg_build_dir}

%files
%defattr(-,root,root)
%doc %docdir
%config(noreplace) %sysconfdir/logrotate.d/*
%config(noreplace) %confdir/*
%sysconfdir/profile.d/*
%liblsb/oracle-base-functions
/etc/rc.d/init.d/oracle
/var/log/oracle/*

%files restart
%defattr(-,root,root)
%liblsb/oracle-restart-functions
/etc/rc.d/init.d/oracle-restart

%files grid
%defattr(-,root,root)
%liblsb/oracle-grid-functions
/etc/rc.d/init.d/oracle-grid

%files listener
%defattr(-,root,root)
%liblsb/oracle-listener-functions
/etc/rc.d/init.d/oracle-listener

%files asm
%defattr(-,root,root)
%liblsb/oracle-asm-functions
/etc/rc.d/init.d/oracle-asm

%files rdbms
%defattr(-,root,root)
%liblsb/oracle-rdbms-functions
/etc/rc.d/init.d/oracle-rdbms

%files dbconsole
%defattr(-,root,root)
%liblsb/oracle-dbconsole-functions
/etc/rc.d/init.d/oracle-dbconsole


%changelog
* Tue Jul 14 2015 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.4-1   11:14:59 +0500
- New upstream release. See ChangeLog for details.

* Tue Dec 09 2014 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.3-1   12:46:28 +0600
- New upstream release. See ChangeLog for details.

* Thu Oct 09 2014 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.2-2   12:46:28 +0600
- New upstream release. See ChangeLog for details.

* Fri Mar 14 2014 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.2-1   12:20:22 +0600
- New upstream release. See ChangeLog for details.

* Fri Oct 18 2013 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.1-2   13:29:49 +0600
- New upstream release

* Wed Dec 26 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-22  11:46:00 +0600
- New upstream release

* Wed Oct 10 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-21  10:18:14 +0600
- Run pre-,postscripts in oracle-dbconsole as ORA_OWNER user

* Fri Oct 05 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-20  12:34:17 +0600
- New upstream release

* Thu Sep 13 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-19  10:47:33 +0600
- New upstream release

* Mon Sep 10 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-18  16:27:49 +0600
- New upstream release

* Thu Aug 23 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-17  12:15:27 +0600
- New upstream release

* Tue Aug 21 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-16  16:12:06 +0600
- New upstream release

* Tue Aug 21 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-15  15:11:34 +0600
- New upstream release

* Tue Jul 10 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-14  12:22:05 +0600
- New upstream release

* Thu Jul 05 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-13  17:49:24 +0600
- New order for start/stop init.d scripts

* Tue Jul 03 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12.4  17:55:09 +0600
- Fixed errors in package scripts for Debian

* Tue Jul 03 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12.3  17:15:03 +0600
- New upstream release
- Fix in dbconsole startup script

* Tue Jul 03 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12.2  16:25:39 +0600
- New upstream release
- Another little fix in dbconsole package

* Tue Jul 03 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12.1  16:06:09 +0600
- New upstream release

* Mon Jul 02 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12  13:12:19 +0600
- New upstream release

* Tue Jun 19 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-11  18:27:30 +0600
- New upstream release

* Tue Jun 19 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-10  16:11:09 +0600
- New upstream release

* Fri Jun 15 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-9  17:35:39 +0600
- Fix dependecy to initscripts

* Thu Jun 14 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-8  13:12:23 +0600
- New upstream release

* Sat Jun 09 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-7  13:23:11 +0600
- New upstream release

* Wed May 23 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-6  13:17:58 +0600
- New upstream release

* Fri Apr 27 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-5  15:07:49 +0600
- New upstream release

* Fri Apr 27 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-4  12:24:22 +0600
- New upstream release

* Thu Apr 26 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-3  18:12:23 +0600
- New upstream release

* Thu Apr 26 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-2  11:14:48 +0600
- New upstream release

* Fri Apr 20 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-1  12:35:02 +0600
- Initial version for RedHat Linux.

