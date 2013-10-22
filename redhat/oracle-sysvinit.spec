Summary   : Start/stop Oracle services.
Summary(ru_RU.UTF-8): Скрипты пуска/останова сервисов Oracle.
Name      : oracle-sysvinit
Version   : 1.1
Release   : 2
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
%define lsbdir          /lib/lsb
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
  --with-lsbdir=%lsbdir --with-confdir=%confdir --with-logdir=%logdir

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
%lsbdir/oracle-base-functions
/etc/rc.d/init.d/oracle
/var/log/oracle/*

%files restart
%defattr(-,root,root)
%lsbdir/oracle-restart-functions
/etc/rc.d/init.d/oracle-restart

%files grid
%defattr(-,root,root)
%lsbdir/oracle-grid-functions
/etc/rc.d/init.d/oracle-grid

%files listener
%defattr(-,root,root)
%lsbdir/oracle-listener-functions
/etc/rc.d/init.d/oracle-listener

%files asm
%defattr(-,root,root)
%lsbdir/oracle-asm-functions
/etc/rc.d/init.d/oracle-asm

%files rdbms
%defattr(-,root,root)
%lsbdir/oracle-rdbms-functions
/etc/rc.d/init.d/oracle-rdbms

%files dbconsole
%defattr(-,root,root)
%lsbdir/oracle-dbconsole-functions
/etc/rc.d/init.d/oracle-dbconsole


%changelog
* Fri Oct 18 2013 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.1-2   13:29:49 +0600
- Fixed bug [ticket:#4]

* Wed Dec 26 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-22  11:46:00 +0600
- Fix error to get status of oracle XE instance

* Wed Oct 10 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-21  10:18:14 +0600
- Run pre-,postscripts in oracle-dbconsole as ORA_OWNER user

* Fri Oct 05 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-20  12:34:17 +0600
- New status function for oracle dbConsole (OMS)
- Supported arguments for oracle_dbconsole_run_sqlfile

* Thu Sep 13 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-19  10:47:33 +0600
- Fixed bug with return value from while loop

* Mon Sep 10 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-18  16:27:49 +0600
- Return status from init.d scripts
- Get status of dbConsole in force mode

* Thu Aug 23 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-17  12:15:27 +0600
- Fixed error in oracle_debug function

* Tue Aug 21 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-16  16:12:06 +0600
- Fixed error in oracle_dbconsole_prestart and oracle_dbconsole_poststart

* Tue Aug 21 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-15  15:11:34 +0600
- Fixed error in dbconsole_get_emhome function name

* Tue Jul 10 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-14  12:22:05 +0600
- Add force mode to setup ORACLE environment in dbConsole functions

* Thu Jul 05 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-13  17:49:24 +0600
- New order for start/stop init.d scripts

* Tue Jul 03 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12.4  17:55:09 +0600
- Fixed errors in package scripts for Debian

* Tue Jul 03 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12.3  17:15:03 +0600
- Fix in dbconsole startup script

* Tue Jul 03 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12.2  16:25:39 +0600
- Another little fix in dbconsole package

* Tue Jul 03 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12.1  16:06:09 +0600
- Little fix in dbconsole package

* Mon Jul 02 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-12  13:12:19 +0600
- Fixed bug in oracle_listener_is_oracle_restart_resource

* Tue Jun 19 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-11  18:27:30 +0600
- Fixed bug in oracle_rdbms_is_oracle_restart_resource

* Tue Jun 19 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-10  16:11:09 +0600
- oracle_orahome_patchset_version function to check PatchSets version

* Fri Jun 15 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-9  17:35:39 +0600
- Fix dependecy to initscripts

* Thu Jun 14 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-8  13:12:23 +0600
- Check whether RDBMS service is Oracle Restart Resource
- Check whether Listener service is Oracle Restart Resource

* Sat Jun 09 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-7  13:23:11 +0600
- Fix error while removing old ORACLE_HOME from PATH

* Wed May 23 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-6  13:17:58 +0600
- More reliable way to get RDBMS ORAHOME version

* Fri Apr 27 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-5  15:07:49 +0600
- oracle_orahome_version get full version of oracle.server component

* Fri Apr 27 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-4  12:24:22 +0600
- oracle_orahome_version function is added

* Thu Apr 26 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-3  18:12:23 +0600
- Fix error in control dbConsole service

* Thu Apr 26 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-2  11:14:48 +0600
- Fix error when remove /etc/rc?.d/*ohasd files

* Fri Apr 20 2012 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-1  12:35:02 +0600
- Initial version for RedHat Linux.

